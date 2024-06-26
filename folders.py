import os
import shutil

def organize_yaml_files(files_per_folder=1000):
    # Get the current working directory
    src_dir = os.getcwd()
    
    # Get list of all YAML files in the current directory
    yaml_files = [f for f in os.listdir(src_dir) if f.endswith('.yaml')]
    
    # Sort the files to ensure consistent ordering
    yaml_files.sort()
    
    # Calculate the number of folders needed
    num_folders = (len(yaml_files) + files_per_folder - 1) // files_per_folder
    
    for folder_idx in range(num_folders):
        # Create a new folder in the current directory
        dst_dir = os.path.join(src_dir, str(folder_idx + 1))
        os.makedirs(dst_dir, exist_ok=True)
        
        # Calculate the range of files for this folder
        start_idx = folder_idx * files_per_folder
        end_idx = min(start_idx + files_per_folder, len(yaml_files))
        
        # Move the files into the new folder
        for file_idx in range(start_idx, end_idx):
            src_file = os.path.join(src_dir, yaml_files[file_idx])
            dst_file = os.path.join(dst_dir, yaml_files[file_idx])
            shutil.move(src_file, dst_file)
    
    print(f"Organized {len(yaml_files)} YAML files into {num_folders} folders.")

# Run the script
organize_yaml_files()
