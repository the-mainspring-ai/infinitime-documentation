#!/usr/bin/env python3

import os
import re
from pathlib import Path


def fix_duplicate_titles(file_path):
    """Fix duplicate titles in markdown files where there's a plain text title followed by the same header."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern to match: a line followed by a header with the same text
    # This handles both cases where there might be whitespace or not
    pattern = r"^([^\n#]+)\n# \1\n"

    # Replace with just the header version
    new_content = re.sub(pattern, r"# \1\n", content, flags=re.MULTILINE)

    # Only write if changes were made
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False


def process_directory(directory):
    """Process all markdown files in the given directory and its subdirectories."""
    fixed_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                if fix_duplicate_titles(file_path):
                    fixed_files.append(file_path)
    return fixed_files


if __name__ == "__main__":
    # Get the docs directory from the current working directory
    docs_dir = "docs"

    if not os.path.exists(docs_dir):
        print(f"Error: {docs_dir} directory not found")
        exit(1)

    print(f"Processing markdown files in {docs_dir}...")
    fixed_files = process_directory(docs_dir)

    if fixed_files:
        print("\nFixed duplicate titles in the following files:")
        for file in fixed_files:
            print(f"- {file}")
    else:
        print("\nNo files needed fixing.")
