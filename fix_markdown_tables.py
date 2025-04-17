#!/usr/bin/env python3
import os
import re

"""
This script fixes formatting issues in markdown tables within documentation files.
It ensures consistent table formatting by:
1. Adding proper pipe (|) characters at the start and end of each row
2. Ensuring consistent spacing around pipe characters
3. Adding or fixing table separators (the row with dashes)
4. Maintaining proper column alignment

The script processes all markdown files in the docs/output_md/InfiniTime/help_file directory
and its subdirectories, fixing any table formatting issues it finds.

Features:
- Cleans up whitespace around pipe characters
- Ensures each row starts and ends with a pipe
- Adds or fixes table separators with proper column count
- Preserves non-table content

Usage:
    Run the script: python fix_markdown_tables.py
"""


def clean_table_row(row):
    """Clean up a table row by ensuring proper pipe formatting"""
    # Remove whitespace around the row
    row = row.strip()
    # Ensure row starts with pipe
    if not row.startswith("|"):
        row = "| " + row
    # Ensure row ends with pipe
    if not row.endswith("|"):
        row = row + " |"
    # Clean up spacing around pipes
    row = re.sub(r"\|\s*", "| ", row)
    row = re.sub(r"\s*\|", " |", row)
    return row


def fix_table_formatting(content):
    # Split content into lines
    lines = content.split("\n")
    fixed_lines = []
    i = 0
    in_table = False

    while i < len(lines):
        line = lines[i].rstrip()

        # Skip empty lines
        if not line:
            fixed_lines.append(line)
            i += 1
            continue

        # Check if this line is part of a table
        if "|" in line:
            # Clean up the row formatting
            line = clean_table_row(line)

            # If this is the start of a table
            if not in_table:
                in_table = True
                header = line
                fixed_lines.append(header)

                # Count columns
                columns = len([x for x in header.split("|") if x.strip()])

                # Check if next line is a proper separator
                if (
                    i + 1 < len(lines)
                    and "|" in lines[i + 1]
                    and all(
                        ("-" in cell)
                        for cell in lines[i + 1].split("|")
                        if cell.strip()
                    )
                ):
                    # Separator exists, but clean it up
                    i += 1
                    separator = "|" + "|".join([" --- " for _ in range(columns)]) + "|"
                    fixed_lines.append(separator)
                else:
                    # Add separator
                    separator = "|" + "|".join([" --- " for _ in range(columns)]) + "|"
                    fixed_lines.append(separator)
            else:
                # This is a continuation of the table
                fixed_lines.append(line)
        else:
            # Not a table row
            in_table = False
            fixed_lines.append(line)
        i += 1

    return "\n".join(fixed_lines)


def process_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Only process if file contains tables
        if "|" in content:
            fixed_content = fix_table_formatting(content)
            if fixed_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(fixed_content)
                print(f"Fixed tables in: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")


def main():
    base_dir = "docs/output_md/InfiniTime/help_file"

    # Walk through all directories
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                process_file(file_path)


if __name__ == "__main__":
    main()
