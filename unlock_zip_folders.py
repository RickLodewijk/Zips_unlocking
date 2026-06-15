import os
import zipfile
import shutil
import tempfile

# Configuration - Replace placeholders with your actual paths
MAIN_ZIP_PATH = "path/to/your/main.zip"
OUTPUT_FOLDER = "path/to/your/output_folder"

def extract_swf_from_zips(zip_path, target_dir):
    """
    Extracts all .swf files from a main zip file and any nested sub-zip files.
    """
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"Created output directory: {target_dir}")

    # Use a temporary directory to unpack the contents
    with tempfile.TemporaryDirectory() as temp_dir:
        print("Extracting main zip file...")
        with zipfile.ZipFile(zip_path, 'r') as main_zip:
            main_zip.extractall(temp_dir)

        # Walk through all files extracted from the main zip
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                
                # If it's a nested sub-zip, extract its content as well
                if file.lower().endswith('.zip'):
                    try:
                        with zipfile.ZipFile(file_path, 'r') as sub_zip:
                            for sub_file in sub_zip.namelist():
                                if sub_file.lower().endswith('.swf'):
                                    # Get the base filename and save it to the target directory
                                    base_name = os.path.basename(sub_file)
                                    if base_name:  # Check if it's a file and not a directory
                                        with sub_zip.open(sub_file) as source, \
                                             open(os.path.join(target_dir, base_name), 'wb') as dest:
                                            shutil.copyfileobj(source, dest)
                                            print(f"Extracted: {base_name}")
                    except zipfile.BadZipFile:
                        print(f"Warning: Could not open {file} (corrupted zip file).")
                
                # If a loose .swf file is already present in the main zip, copy it directly
                elif file.lower().endswith('.swf'):
                    shutil.copy(file_path, os.path.join(target_dir, file))
                    print(f"Copied standalone SWF: {file}")

    print("\nDone! All .swf files have been extracted to your output folder.")

if __name__ == "__main__":
    extract_swf_from_zips(MAIN_ZIP_PATH, OUTPUT_FOLDER)