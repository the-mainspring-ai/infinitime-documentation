import os
import re
from pathlib import Path

# Set the base URL to use when converting relative PDF URLs into absolute ones.
BASE_PDF_URL = "https://version9.infinitimeonline.net/InfiniTime/"


def find_md_files(directory):
    """
    Recursively find all markdown (.md) files in the given directory.
    """
    return list(Path(directory).rglob("*.md"))


def extract_pdf_links(content):
    """
    Extract all markdown links that reference a PDF file.
    Matches markdown links like: [Some Text](some/path/file.pdf)
    Optionally supports query parameters or anchors.
    """
    pattern = r"\[.*?\]\(([^)]+\.pdf(?:\?[^)\s]*)?(?:#[^)]+)?)\)"
    pdf_links = re.findall(pattern, content, re.IGNORECASE)
    return pdf_links


def find_original_pdf_url(pdf_filename, processed_dir):
    """
    Search within all HTML files in the processed_docs_with_images directory for
    an anchor (<a ... href="...">) whose href attribute contains the given pdf_filename.
    Returns the first matching URL as a string, or None if not found.
    """
    regex = re.compile(
        r'href=["\'](.*?{}(?:\?[^"\']*)?(?:#[^"\']*)?)["\']'.format(
            re.escape(pdf_filename)
        ),
        re.IGNORECASE,
    )

    for html_file in Path(processed_dir).rglob("*.html"):
        try:
            with open(html_file, "r", encoding="utf-8") as f:
                content = f.read()
            match = regex.search(content)
            if match:
                found_url = match.group(1)
                print(
                    f"  Found original URL for '{pdf_filename}' in '{html_file}': {found_url}"
                )
                return found_url
        except Exception as e:
            print(f"  Error reading '{html_file}': {e}")
    return None


def fix_pdf_urls_in_file(md_file_path, processed_dir):
    """
    In the given markdown file, find PDF URL links that are likely being misprocessed.
    Replace the relative PDF URLs with the correct full, absolute URL as found in the processed HTML docs.

    Returns True if at least one replacement was made.
    """
    with open(md_file_path, "r", encoding="utf-8") as f:
        content = f.read()

    pdf_links = extract_pdf_links(content)
    if not pdf_links:
        # No PDF links found in this file
        return False

    print(f"\nProcessing file: {md_file_path}")
    print("PDF links found:")
    for link in pdf_links:
        print(f"  {link}")

    content_modified = content
    made_replacement = False

    for pdf_link in pdf_links:
        # Only process non-absolute URLs (skip if the URL starts with http:// or https://)
        if pdf_link.lower().startswith("http"):
            continue

        pdf_filename = os.path.basename(pdf_link)
        original_url = find_original_pdf_url(pdf_filename, processed_dir)
        if original_url:
            # If the URL is still relative, convert it to an absolute URL.
            if not original_url.lower().startswith("http"):
                # Look for the folder name 'RESOURCES' in the URL.
                idx = original_url.find("RESOURCES")
                if idx != -1:
                    original_url = BASE_PDF_URL + original_url[idx:]
                else:
                    # If not found, you might choose to skip or warn.
                    print(
                        f"WARNING: Relative URL does not contain 'RESOURCES': {original_url}"
                    )

            # Replace spaces in the URL with %20
            original_url = original_url.replace(" ", "%20")

            print(f"Replacing '{pdf_link}' with '{original_url}'")
            content_modified = content_modified.replace(pdf_link, original_url)
            made_replacement = True
        else:
            print(f"WARNING: No original URL found for '{pdf_filename}'")

    if made_replacement:
        with open(md_file_path, "w", encoding="utf-8") as f:
            f.write(content_modified)
        print(f"Updated file: {md_file_path}")
        return True

    return False


def main():
    # Adjust these paths as needed.
    # This directory should contain your markdown files that are processed by Docusaurus.
    md_directory = Path("docs/output_md")
    # This directory contains the original HTML docs that have the proper PDF URLs.
    processed_directory = Path("processed_docs_with_images")

    md_files = find_md_files(md_directory)
    print(f"Found {len(md_files)} markdown files to check.")

    fixed_files_count = 0

    for md_file in md_files:
        if fix_pdf_urls_in_file(md_file, processed_directory):
            fixed_files_count += 1

    print(f"\nFixed PDF links in {fixed_files_count} markdown file(s).")


if __name__ == "__main__":
    main()
