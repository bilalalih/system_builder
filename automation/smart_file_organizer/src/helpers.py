import os
import shutil
from src.rules import FOLDERS

def get_files():
    # Asks the user for the number of files 
    no_of_files = input("How many files do you want to organize?: ")
    num = int(no_of_files)
    files = []
    # Loops through while asking the user for a file
    for file in range(num):
        file = input("file?: ")
        files.append(file)

    return files

def sort_files(files, folder_name:str):
    os.mkdir(folder_name)
    for file in files:
        # Checks if file in files exists
        if os.path.exists(file):
           if os.path.isfile(file):
                ext = os.path.splitext(file)[1].lower()
                for folder, exts in FOLDERS.items():
                    if ext in exts:
                        # Create folder
                        os.makedirs(f'{folder_name}/{folder}', exist_ok=True)
                        shutil.move(file, f"{folder_name}/{folder}/{file}")
                        print(f"Moved {file} to {folder_name}/{folder}")
                        break