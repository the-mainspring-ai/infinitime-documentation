import os
import re

# Directories
docs_dir = "docs"  # Directory containing Markdown files (may include subdirectories)
html_root_dir = "processed_docs_with_images"  # All corresponding HTML files are in this flat directory

# The placeholder image path in the Markdown files.
placeholder = "static/img/image-404.png"


def find_corresponding_html(md_base):
    """
    Construct the expected HTML file name by appending '_processed.html' to the Markdown base name.
    Check if it exists in the html_root_dir.
    """
    html_filename = f"{md_base}_processed.html"
    html_path = os.path.join(html_root_dir, html_filename)
    if os.path.exists(html_path):
        return html_path
    else:
        return None


def extract_actual_image(html_path):
    """
    Open the HTML file and search for the first image link that is not the placeholder.
    Returns the image file name (e.g., 'actual_image.png') or None if not found.
    """
    with open(html_path, "r", encoding="utf8") as f:
        html_content = f.read()

    # The regex matches any image URL in static/img/ that is not 'image-404.png'
    match = re.search(r'static/img/((?!image-404\.png)[^"\'\s]+)', html_content)
    if match:
        return match.group(1)
    return None


def update_markdown_image(md_path, actual_image):
    """
    Replace the placeholder image with the actual image in the Markdown file.
    """
    with open(md_path, "r", encoding="utf8") as f:
        md_content = f.read()

    if placeholder in md_content:
        new_image_path = f"static/img/{actual_image}"
        updated_content = md_content.replace(placeholder, new_image_path)
        with open(md_path, "w", encoding="utf8") as f:
            f.write(updated_content)
        print(f"Updated {md_path} with {new_image_path}")
    else:
        print(f"No placeholder found in {md_path}")


def main():
    # Walk recursively through all Markdown files in docs_dir.
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.lower().endswith(".md"):
                md_path = os.path.join(root, file)
                md_base = os.path.splitext(file)[0]

                # Construct the corresponding HTML file name and check for its existence.
                html_path = find_corresponding_html(md_base)
                if not html_path:
                    print(f"HTML file for {md_path} not found.")
                    continue

                # Extract the actual image name from the HTML file.
                actual_image = extract_actual_image(html_path)
                if not actual_image:
                    print(f"No valid image link found in HTML {html_path}")
                    continue

                # Update the Markdown file with the actual image.
                update_markdown_image(md_path, actual_image)


if __name__ == "__main__":
    main()
