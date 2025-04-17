"""
This script crawls and downloads content from the InfiniTime online documentation website,
converting HTML pages to markdown format while preserving the document structure and downloading
associated images. It creates a local copy of the documentation with proper markdown formatting
and local image references.

The script performs the following operations:
1. Crawls the InfiniTime documentation website starting from a specified URL
2. Downloads and converts HTML pages to markdown format
3. Downloads and stores images locally
4. Updates image references in the markdown to point to local files
5. Maintains the original directory structure
6. Handles internal links and navigation

Configuration:
- base_url: Base URL of the InfiniTime documentation
- start_url: Initial URL to start crawling from
- output_dir: Directory where markdown files will be saved
- images_dir: Directory where images will be stored

Features:
- Recursive crawling of internal links
- Image downloading and local storage
- HTML to markdown conversion
- Link rewriting for local navigation
- Error handling and logging

Dependencies:
- requests: For HTTP requests
- beautifulsoup4: For HTML parsing
- markdownify: For HTML to markdown conversion

Usage:
    Run the script: python download-content.py
"""

import os
import requests
from collections import deque
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from markdownify import markdownify as md_convert

# Base parameters
base_url = "https://infinitimeonline.net/"
start_url = "https://infinitimeonline.net/InfiniTime/help%20file/TC32.htm"
output_dir = "output_md_2"
images_dir = os.path.join(output_dir, "images_2")

# Create output directories
os.makedirs(output_dir, exist_ok=True)
os.makedirs(images_dir, exist_ok=True)

# Data structures for crawling
visited = set()  # normalized URLs already processed
to_visit = deque([start_url])  # Queue of URLs to process


def normalize_url(url: str) -> str:
    """
    Normalizes a URL by stripping the fragment.
    """
    parsed = urlparse(url)
    normalized = parsed._replace(fragment="").geturl()
    return normalized


def is_internal(url: str) -> bool:
    """
    Returns True if the URL belongs to the same domain as base_url.
    """
    parsed = urlparse(url)
    base_parsed = urlparse(base_url)
    return (parsed.netloc == base_parsed.netloc) or (parsed.netloc == "")


def safe_filename(url: str) -> str:
    """
    Converts the URL's filename to a safe markdown filename.
    Converts .htm/.html to .md; if not ending with .md, appends .md.
    """
    parsed = urlparse(url)
    path = parsed.path
    if not os.path.basename(path):
        # For URL ending with a slash, mimic a default file (e.g., index.htm)
        path = os.path.join(path, "index.htm")
    filename = os.path.basename(path)
    if filename.lower().endswith(".htm"):
        filename = filename[:-4] + ".md"
    elif filename.lower().endswith(".html"):
        filename = filename[:-5] + ".md"
    elif not filename.lower().endswith(".md"):
        filename += ".md"
    return filename


def save_markdown(content: str, url: str) -> None:
    """
    Saves the given Markdown content into the output file,
    preserving the URL's directory structure.
    """
    parsed = urlparse(url)
    rel_dir = os.path.dirname(parsed.path).lstrip("/")
    # Replace URL-encoded spaces with underscores for file-system compatibility
    rel_dir = rel_dir.replace("%20", "_")
    folder = os.path.join(output_dir, rel_dir)
    os.makedirs(folder, exist_ok=True)

    file_name = safe_filename(url)
    file_path = os.path.join(folder, file_name)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved Markdown: {file_path}")


def download_image(img_url: str) -> str:
    """
    Downloads an image (if not already downloaded) and returns the relative path.
    """
    image_path = urlparse(img_url).path
    image_name = os.path.basename(image_path)
    local_image_path = os.path.join(images_dir, image_name)

    if not os.path.exists(local_image_path):
        print(f"Downloading image: {img_url}")
        try:
            img_response = requests.get(img_url)
            if img_response.ok:
                with open(local_image_path, "wb") as f:
                    f.write(img_response.content)
            else:
                print(f"Warning: Failed to download image from {img_url}")
                return img_url  # Return original URL on failure
        except Exception as e:
            print(f"Exception while downloading {img_url}: {e}")
            return img_url
    rel_path = os.path.relpath(local_image_path, output_dir)
    return rel_path


while to_visit:
    current_url = to_visit.popleft()
    current_url = normalize_url(current_url)  # Normalize to remove fragments
    if current_url in visited:
        continue  # Skip already processed pages
    visited.add(current_url)
    print(f"\nCrawling: {current_url}")

    try:
        response = requests.get(current_url)
        if not response.ok:
            print(f"Error: Could not retrieve page at {current_url}")
            continue
    except Exception as e:
        print(f"Exception for {current_url}: {e}")
        continue

    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    # Process <img> tags: download images and update the src to local paths.
    for img in soup.find_all("img"):
        src = img.get("src")
        if not src:
            continue
        image_url = urljoin(current_url, src)
        new_src = download_image(image_url)
        img["src"] = new_src

    # Process <a> tags: rewrite internal links and queue internal pages.
    for a in soup.find_all("a", href=True):
        href = a.get("href")
        absolute_href = urljoin(current_url, href)
        print(f"Discovered link: {absolute_href}")  # Debug: show discovered link
        if is_internal(absolute_href):
            normalized_href = normalize_url(absolute_href)
            if normalized_href not in visited:
                print(f"Queueing: {normalized_href}")  # Debug: show link being queued
                to_visit.append(normalized_href)
            # Rewriting link to point to markdown version.
            parsed_href = urlparse(absolute_href)
            file_part = parsed_href.path
            if file_part.lower().endswith(".htm"):
                file_part = file_part[:-4] + ".md"
            elif file_part.lower().endswith(".html"):
                file_part = file_part[:-5] + ".md"
            anchor = parsed_href.fragment
            new_href = file_part
            if anchor:
                new_href += "#" + anchor
            a["href"] = new_href

    # Process frames/iframes if they exist.
    for frame in soup.find_all(["frame", "iframe"]):
        src = frame.get("src")
        if src:
            absolute_src = urljoin(current_url, src)
            print(f"Discovered frame/iframe link: {absolute_src}")  # Debug print
            if is_internal(absolute_src):
                normalized_src = normalize_url(absolute_src)
                if normalized_src not in visited:
                    print(f"Queueing frame/iframe: {normalized_src}")  # Debug print
                    to_visit.append(normalized_src)

    # Convert modified HTML to Markdown.
    markdown_content = md_convert(str(soup), heading_style="ATX")
    save_markdown(markdown_content, current_url)

print("Crawling complete.")
