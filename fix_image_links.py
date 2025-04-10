#!/usr/bin/env python3
import os
import re
import shutil
from pathlib import Path

# Paths configuration
CORRECT_MD_PATH = "output_md_2/InfiniTime/help_file"
WORKING_MD_PATH = "docs/output_md/InfiniTime/help_file"
IMAGE_PATH = "static/img"

# Regular expressions for image detection
BROKEN_IMAGE_PATTERN = r"!\[\]\(/img/image-404\.png\)"
# Match both images_2/ pattern and any other image patterns
CORRECT_IMAGE_PATTERN_1 = r"!\[\]\(images_2/([^)]+)\)"
CORRECT_IMAGE_PATTERN_2 = r"!\[\]\(([^)]+\.(?:gif|jpg|png|jpeg))\)"

def get_md_files(directory):
    """Returns a list of all markdown files in the given directory and subdirectories."""
    return list(Path(directory).glob("**/*.md"))

def check_image_exists(image_name):
    """Check if the image exists in the static/img directory."""
    return os.path.exists(os.path.join(IMAGE_PATH, image_name))

def extract_filename(path):
    """Extract just the filename from a path, handling various formats."""
    # Remove any directory structure and get just the filename
    return os.path.basename(path)

def process_files():
    """Process all markdown files and update image references."""
    correct_md_files = get_md_files(CORRECT_MD_PATH)
    updates_made = 0
    skipped_files = 0
    files_processed = 0
    images_not_found = set()
    
    for correct_file_path in correct_md_files:
        # Determine the corresponding working file path
        relative_path = correct_file_path.relative_to(CORRECT_MD_PATH)
        working_file_path = Path(WORKING_MD_PATH) / relative_path
        
        if not working_file_path.exists():
            print(f"Working file does not exist: {working_file_path}")
            skipped_files += 1
            continue
        
        # Read both files
        with open(correct_file_path, 'r', encoding='utf-8') as f:
            correct_content = f.read()
        
        with open(working_file_path, 'r', encoding='utf-8') as f:
            working_content = f.read()
        
        # Find all image references in the correct file
        correct_images_1 = re.findall(CORRECT_IMAGE_PATTERN_1, correct_content)
        correct_images_2 = re.findall(CORRECT_IMAGE_PATTERN_2, correct_content)
        # Combine both lists and remove duplicates
        correct_images = list(set(correct_images_1 + correct_images_2))
        
        # If there are no image references in the correct file, skip
        if not correct_images:
            print(f"No image references found in: {correct_file_path}")
            skipped_files += 1
            continue
        
        # Count broken images in working file
        broken_images_count = len(re.findall(BROKEN_IMAGE_PATTERN, working_content))
        
        if broken_images_count == 0:
            print(f"No broken images found in: {working_file_path}")
            skipped_files += 1
            continue
        
        # Process and replace images
        updated_content = working_content
        replacements_made = 0
        
        # For each image in the correct content, try to update a broken image
        for image_path in correct_images:
            # Extract just the filename
            image_name = extract_filename(image_path)
            
            # Check if the image exists in the static/img directory
            if check_image_exists(image_name):
                # Replace one instance of the broken image pattern with the correct image path
                # Only replace if we still have broken images to fix
                if replacements_made < broken_images_count:
                    new_content = re.sub(
                        BROKEN_IMAGE_PATTERN, 
                        f"![](/img/{image_name})", 
                        updated_content, 
                        count=1
                    )
                    
                    # Only count as a replacement if something changed
                    if new_content != updated_content:
                        updated_content = new_content
                        replacements_made += 1
                        print(f"  - Replaced broken image with {image_name}")
            else:
                images_not_found.add(image_name)
        
        # If content was modified, write it back to the file
        if updated_content != working_content:
            with open(working_file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            print(f"Updated {replacements_made} images in: {working_file_path}")
            updates_made += 1
        else:
            print(f"No updates needed for: {working_file_path}")
            skipped_files += 1
        
        files_processed += 1
    
    print(f"\nSummary:")
    print(f"Files processed: {files_processed}")
    print(f"Files updated: {updates_made}")
    print(f"Files skipped: {skipped_files}")
    
    if images_not_found:
        print(f"\nThe following images were referenced but not found in {IMAGE_PATH}:")
        for img in sorted(images_not_found):
            print(f"  - {img}")

if __name__ == "__main__":
    if not os.path.exists(CORRECT_MD_PATH):
        print(f"Error: Correct MD path does not exist: {CORRECT_MD_PATH}")
    elif not os.path.exists(WORKING_MD_PATH):
        print(f"Error: Working MD path does not exist: {WORKING_MD_PATH}")
    elif not os.path.exists(IMAGE_PATH):
        print(f"Error: Image path does not exist: {IMAGE_PATH}")
    else:
        print(f"Starting image link fix process...")
        process_files()
        print("Done!") 