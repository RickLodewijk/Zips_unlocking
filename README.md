# SWF Extractor from Nested Zips

A lightweight Python script designed to automatically traverse a main ZIP archive, find any nested sub-ZIP files, and extract all `.swf` (Shockwave Flash) files into a single designated output folder. It also copies any standalone `.swf` files found directly within the main archive.

## Features

- **Recursive Extraction:** Extracts `.swf` files from both the main ZIP and any ZIP files contained *inside* it.
- **Flattens Output:** Collects all discovered `.swf` files and saves them into a single flat directory for easy access.
- **Safe Extraction:** Uses Python's `tempfile` module to handle intermediate extraction in a secure, isolated temporary directory.
- **Corrupted Zip Handling:** Gracefully skips and logs warnings for corrupted or unreadable sub-ZIP files without crashing the execution.

## Prerequisites

- Python 3.x
- No external dependencies required (uses built-in standard libraries: `os`, `zipfile`, `shutil`, `tempfile`).

## Usage

1. Clone or download this repository.
2. Open `swf_extractor.py` in a text editor.
3. Configure your paths at the top of the script:
   ```python
   MAIN_ZIP_PATH = "path/to/your/main.zip"
   OUTPUT_FOLDER = "path/to/your/output_folder"
