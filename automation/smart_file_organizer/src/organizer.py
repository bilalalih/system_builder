from src.helpers import get_files, sort_files
                    
def organize_directory():
    while True:
        files = get_files()
        crt = input("Create Folder(y/n)")
        print(files)
        if crt == 'y':
            folder_name = input("Name:")
            try:
                sort_files(files, folder_name)
            except:
                print("Sorting failed")
            break
        else:
            break

