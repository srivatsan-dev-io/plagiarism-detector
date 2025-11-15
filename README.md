# Simple Plagiarism Detector

This is a simple command line tool written in Python that compares the text content of two files and gives you a score of their similarity. It is very useful for quickly checking for potential plagiarism or content duplication.


## Key Features

* **Easy to Use:** Works from your command line (terminal).
* **File Path Check:** It makes sure the files actually exist before trying to read them.
* **Clean Input:** It automatically ignores extra spaces or quotes
* **Similarity Score:** It calculates a ratio (a number between **0.0 and 1.0**).

## How It Calculates Similarity

The tool uses Python's difflib.SequenceMatcher class to compare the text in both files character-by-character.

The output score is the Similarity Ratio**:

* **1.0:** The files are **exactly the same**.
* **0.0:** The files share **no common content**.
* A score like **0.90** suggests a very high degree of similarity or potential copy-pasting.

## Requirements

Python must be installed in the system.
