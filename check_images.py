"""
This script checks and fixes image references in markdown documentation files to ensure they
are compatible with Docusaurus's image handling. It verifies the existence of images in the
static/img directory and updates references accordingly.

The script performs the following operations:
1. Finds all markdown files in the documentation directory
2. Extracts image references from each markdown file
3. Checks if referenced images exist in the static/img directory
4. Updates image references to use Docusaurus-compliant absolute paths
5. Replaces missing images with a placeholder image

Configuration:
- docs_dir: Directory containing markdown files to be processed
- static_img_dir: Directory containing the actual image files

Features:
- Handles both markdown and HTML image syntax
- Converts relative paths to absolute paths
- Provides placeholder for missing images
- Maintains detailed logging of changes
- Preserves original file structure

Usage:
    Run the script: python check_images.py
"""

import os
import re
from pathlib import Path


def find_markdown_files(directory):
    """Find all markdown files in the given directory and its subdirectories."""
    return list(Path(directory).rglob("*.md"))


def extract_image_paths(content):
    """Extract image paths from markdown content.

    Captures both markdown syntax ![alt](path) and HTML <img src="path">.
    """
    img_pattern = r'!\[.*?\]\((.*?)\)|<img[^>]+src=[\'"](.*?)[\'"]'
    matches = re.finditer(img_pattern, content)
    return [
        match.group(1) or match.group(2)
        for match in matches
        if match.group(1) or match.group(2)
    ]


def check_and_replace_images(file_path, static_img_dir):
    """Adjust image references in the markdown file to use Docusaurus-compliant absolute paths.

    - If an image exists in the static_img_dir, update its link to `/img/<filename>`.
    - Otherwise, replace it with `/img/image-404.png` to serve as a placeholder.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    image_paths = extract_image_paths(content)
    replacements_made = False

    print(f"Checking images in {file_path}")

    for img_path in image_paths:
        # Skip if the image path is already in the correct absolute format.
        if img_path.startswith("/img/"):
            continue

        # Extract the image filename (ignore any folder structure in the markdown).
        img_filename = os.path.basename(img_path)
        # Construct the full filesystem path to the image in static/img.
        img_static_path = os.path.join(static_img_dir, img_filename)
        print(f"Processing image: {img_path}")
        print(f"Checking existence of: {img_static_path}")

        # Choose the proper replacement path.
        if os.path.exists(img_static_path):
            replacement_path = f"/img/{img_filename}"
            print(f"Image found. Replacing '{img_path}' with '{replacement_path}'")
        else:
            replacement_path = "/img/image-404.png"
            print(
                f"Image not found. Replacing '{img_path}' with placeholder '{replacement_path}'"
            )

        # Replace the old image path with the new absolute path.
        content = content.replace(img_path, replacement_path)
        replacements_made = True

    # Update the file if any replacement was made.
    if replacements_made:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated file: {file_path}")


def main():
    # 'docs' contains your markdown files,
    # 'static/img' contains all your images.
    docs_dir = Path("docs")
    static_img_dir = Path("static/img")

    # Find all markdown files within the docs directory.
    markdown_files = find_markdown_files(docs_dir)
    print(f"Found {len(markdown_files)} markdown files")

    # Process each markdown file.
    for file_path in markdown_files:
        check_and_replace_images(file_path, static_img_dir)


if __name__ == "__main__":
    main()
