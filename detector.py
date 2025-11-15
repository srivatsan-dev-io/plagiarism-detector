import os
import difflib
from difflib import SequenceMatcher

def get_file_path(prompt_message):

    while True:
        # Getting input and cleaning up
        file_path = input(prompt_message)
        file_path = file_path.strip().strip('"').strip("'")
        
        if os.path.isfile(file_path):
            return file_path
        else:
            print("Error: File not found. Please try again.")

print("Simple Python CLI based Plagiarism Checker")

# Get file paths
file_path_one = get_file_path("\nEnter the full path for the FIRST file: ")
file_path_two = get_file_path("Enter the full path for the SECOND file: ")

with open(file_path_one, 'r') as file_one, open(file_path_two, 'r') as file_two:
    
    content_one = file_one.read()
    content_two = file_two.read()
    
    matcher = SequenceMatcher(None, content_one, content_two)
    similarity_ratio = matcher.ratio()
    print(f"Similarity Ratio: {similarity_ratio:.4f}")