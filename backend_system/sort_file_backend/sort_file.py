import os
import shutil

def sort_files(path:str):
    folders = {
                "code": {'.py', '.cpp', '.java'},
                "data": {'.csv', '.db'},
                "docs": {'.docx', 'txt'},
                "media": {'.jpg', '.mp4', '.png'}
    }
    # Sort files
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            ext = os.path.splitext(file)[1].lower()
            for folder, exts in folders.items():
                if ext in exts:
                    # Create folder if missing
                    os.makedirs(os.path.join(path, folder), exist_ok=True)
                    shutil.move(os.path.join(path, file), os.path.join(path, folder, file))
                    print(f"Moved {file} to {folder}")
                    break