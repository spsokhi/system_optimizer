import os
import shutil

def clean_temp_files(output_callback=print):
    temp_dirs = [os.getenv('TEMP'), r'C:\Windows\Temp']
    
    for temp_dir in temp_dirs:
        if os.path.exists(temp_dir):
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                        output_callback(f"Deleted {file_path}")
                    except PermissionError:
                        output_callback(f"Permission denied: {file_path}. Skipping.")
                    except FileNotFoundError:
                        output_callback(f"File not found: {file_path}. Skipping.")
                    except Exception as e:
                        output_callback(f"Error deleting {file_path}: {e}")
