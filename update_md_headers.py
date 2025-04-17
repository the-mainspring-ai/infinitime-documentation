"""
This script updates markdown files in the documentation by adding or updating their frontmatter headers.
It uses OpenAI's to analyze the content of each markdown file and generate appropriate
title and description metadata. The script processes all markdown files in the docs directory recursively.

The script performs the following operations:
1. Removes any existing XML headers
2. Analyzes the first 1000 characters of content to understand the document's purpose
3. Generates a new frontmatter header with title and description
4. Preserves the original content while adding/updating the header

Dependencies:
- openai: For accessing the OpenAI API
- os, re, glob: For file operations and pattern matching

Usage:
    Ensure OPENAI_API_KEY is set in environment variables
    Run the script: python update_md_headers.py
"""

import os
import re
from openai import OpenAI
import glob

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


def get_document_purpose(content):
    """Use OpenAI API to infer document purpose from content."""
    prompt = f"""Based on the following content, generate a concise markdown title and description.
    Format the response as:
    ---
    title: "Title"
    description: "Description"
    ---
    
    Content:
    {content[:1000]}
    """

    completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that generates markdown frontmatter for documentation files.",
            },
            {"role": "user", "content": prompt},
        ],
        model="gpt-4.1-nano-2025-04-14",  # Using a fast and cost-effective model
        temperature=0.3,
        max_tokens=150,
    )

    return completion.choices[0].message.content


def process_markdown_file(file_path):
    """Process a single markdown file."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove XML header if present
    content = re.sub(r'^<\?xml version="1\.0" encoding="utf-8" \?>\n?', "", content)

    # Get first 100 lines for analysis
    first_100_lines = "\n".join(content.split("\n")[:100])

    # Generate new header using OpenAI
    new_header = get_document_purpose(first_100_lines)

    # Combine new header with content
    updated_content = f"{new_header}\n\n{content.strip()}"

    # Write back to file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"Updated {file_path}")


def main():
    # Find all markdown files in the docs directory
    md_files = glob.glob("docs/**/*.md", recursive=True)

    for file_path in md_files:
        try:
            process_markdown_file(file_path)
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")


if __name__ == "__main__":
    main()
