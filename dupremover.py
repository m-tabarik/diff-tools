import os
import shutil
import hashlib
import sys

def calculate_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    try:
        with open(file_path, 'rb') as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        return file_hash
    except OSError as e:
        print(f"Error calculating hash for {file_path}: {e}")
        return None

def find_yaml_files(root_folder):
    """Traverse directories to find all YAML files."""
    yaml_files = []
    for root, _, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".yaml") or file.endswith(".yml"):
                full_path = os.path.join(root, file)
                yaml_files.append(full_path)
                print(f"Found YAML file: {full_path}")
    return yaml_files

def process_files(yaml_files, destination_folder):
    """Process YAML files, removing duplicates and moving unique ones."""
    unique_files = {}
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created destination folder: {destination_folder}")

    for file_path in yaml_files:
        file_hash = calculate_hash(file_path)
        if file_hash is None:
            continue
        if file_hash not in unique_files:
            unique_files[file_hash] = file_path
            dest_path = os.path.join(destination_folder, os.path.basename(file_path))
            try:
                shutil.move(file_path, dest_path)
                print(f"Unique file moved: {file_path} to {destination_folder}")
            except OSError as e:
                print(f"Error moving file {file_path} to {destination_folder}: {e}")
        else:
            print(f"Duplicate file found: {file_path}, ignoring.")

def main():
    root_folder = os.getcwd()  # Start from the current working directory
    destination_folder = os.path.join(root_folder, "unique_yaml_files")  # Destination folder in the current directory
    
    print("Starting search for YAML files...")
    # Find all YAML files
    yaml_files = find_yaml_files(root_folder)
    
    print("Processing files and removing duplicates...")
    # Process files: remove duplicates and move unique files
    process_files(yaml_files, destination_folder)
    
    print(f"Processing complete. Unique YAML files moved to '{destination_folder}'")

if __name__ == "__main__":
    # Enable long path support for Windows
    if sys.platform == "win32":
        import ctypes
        ctypes.windll.kernel32.SetConsoleCP(65001)
        ctypes.windll.kernel32.SetConsoleOutputCP(65001)
    main()
