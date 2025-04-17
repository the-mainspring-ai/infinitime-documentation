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
- python-dotenv: For loading environment variables from .env file

Usage:
    Ensure OPENAI_API_KEY is set in .env file or environment variables
    Run the script: python update_md_headers.py
"""

import os
import re
from openai import OpenAI
import glob
from dotenv import load_dotenv
import argparse
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


def get_document_purpose(content):
    """Use OpenAI API to infer document purpose from content."""
    prompt = f"""Based on the following content, generate a concise markdown title and description.
    Format the response EXACTLY as shown below with triple dashes at the beginning and end:
    
    ---
    title: "Title"
    description: "Description"
    ---
    
    Ensure the triple dashes are included and proper formatting is maintained.
    
    Content:
    {content[:1000]}
    """

    completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that generates markdown frontmatter for documentation files. Always return properly formatted frontmatter with triple dashes at the beginning and end.",
            },
            {"role": "user", "content": prompt},
        ],
        model="gpt-4.1-nano-2025-04-14",  # Using a fast and cost-effective model
        temperature=0.3,
        max_tokens=150,
    )

    return completion.choices[0].message.content


def process_markdown_file(file_path, dry_run=False):
    """Process a single markdown file."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content

    # Check if XML header is present
    xml_header_match = re.search(
        r'<\?xml\s+version="1\.0"\s+encoding="utf-8"\s*\?>', content
    )
    if xml_header_match:
        logger.info(f"Found XML header in {file_path}")

    # Remove XML header if present
    content = re.sub(
        r'<\?xml\s+version="1\.0"\s+encoding="utf-8"\s*\?>\s*', "", content
    )

    # Check if frontmatter exists
    frontmatter_match = re.search(r"^---\s*\n.*?\n---\s*\n", content, flags=re.DOTALL)
    if frontmatter_match:
        logger.info(f"Found existing frontmatter in {file_path}")

    # Remove existing frontmatter if present (between --- markers)
    content = re.sub(r"^---\s*\n.*?\n---\s*\n", "", content, flags=re.DOTALL)

    # Get first 100 lines for analysis
    first_100_lines = "\n".join(content.split("\n")[:100])

    # Generate new header using OpenAI
    logger.info(f"Generating frontmatter for {file_path}")
    new_header = get_document_purpose(first_100_lines)

    # Log the generated header
    logger.info(f"Generated header: {new_header.strip()}")

    # Ensure the header has proper formatting with triple dashes
    if not new_header.startswith("---"):
        logger.warning(f"Adding missing starting dashes to header in {file_path}")
        new_header = f"---\n{new_header.lstrip('---')}"
    if not new_header.strip().endswith("---"):
        logger.warning(f"Adding missing ending dashes to header in {file_path}")
        new_header = f"{new_header.rstrip('---')}---"

    # Combine new header with content
    updated_content = f"{new_header}\n\n{content.strip()}"

    if dry_run:
        logger.info(f"[DRY RUN] Would update {file_path}")
        return

    # Write back to file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    logger.info(f"Updated {file_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Update markdown files with frontmatter headers"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Run without making changes"
    )
    parser.add_argument(
        "--file", help="Process a specific file instead of all markdown files"
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)

    if args.file:
        logger.info(f"Processing single file: {args.file}")
        process_markdown_file(args.file, dry_run=args.dry_run)
    else:
        # Find all markdown files in the docs directory
        logger.info("Looking for markdown files in docs directory")
        md_files = glob.glob("docs/**/*.md", recursive=True)
        logger.info(f"Found {len(md_files)} markdown files")

        for file_path in md_files:
            try:
                process_markdown_file(file_path, dry_run=args.dry_run)
            except Exception as e:
                logger.error(f"Error processing {file_path}: {str(e)}", exc_info=True)


if __name__ == "__main__":
    main()
