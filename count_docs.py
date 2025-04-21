import os
import re
from collections import defaultdict


def count_words_in_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        # Remove code blocks
        content = re.sub(r"```[\s\S]*?```", "", content)
        # Remove inline code
        content = re.sub(r"`[^`]*`", "", content)
        # Split by whitespace and count non-empty words
        words = [word for word in content.split() if word.strip()]
        return len(words)


def analyze_docs_directory(directory):
    md_files = []
    total_words = 0
    file_word_counts = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                word_count = count_words_in_file(file_path)
                md_files.append(file_path)
                total_words += word_count
                # Store relative path and word count
                rel_path = os.path.relpath(file_path, directory)
                file_word_counts.append((rel_path, word_count))

    return len(md_files), total_words, file_word_counts


if __name__ == "__main__":
    docs_dir = "docs"
    num_files, total_words, file_word_counts = analyze_docs_directory(docs_dir)
    print(f"Number of markdown files: {num_files}")
    print(f"Total number of words: {total_words}")
    print("\nTop 10 longest documents:")
    print("-" * 80)
    print(f"{'File Path':<60} {'Word Count':>10}")
    print("-" * 80)

    # Sort by word count in descending order and get top 10
    for file_path, word_count in sorted(
        file_word_counts, key=lambda x: x[1], reverse=True
    )[:40]:
        print(f"{file_path:<60} {word_count:>10,}")
