# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:35:05 2024

@author: X470118
"""

import os
from docx import Document

def search_docx_files(directory, search_phrase, output_file):
    # List to store file paths that contain the search phrase
    matching_files = []

    # Loop through all files and subdirectories in the specified directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".docx"):
                file_path = os.path.join(root, file)
                try:
                    # Load the .docx file
                    doc = Document(file_path)

                    # Check if the search phrase is found in any paragraph of the document
                    if any(search_phrase.lower() in paragraph.text.lower() for paragraph in doc.paragraphs):
                        matching_files.append(file_path)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    # Write the matching file paths to the output file
    with open(output_file, "w") as f:
        for file_path in matching_files:
            f.write(f"{file_path}\n")

    print(f"Search complete. Results saved to {output_file}")

if __name__ == "__main__":
    # Define the directory to search and the phrase to look for
    directory_to_search = input("Enter the directory to search: ")
    search_phrase = input("Enter the search phrase: ")
    output_file = "search_results.txt"

    search_docx_files(directory_to_search, search_phrase, output_file)
