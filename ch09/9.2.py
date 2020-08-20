import os
path = os.getcwd()

for folder_name, sub_folders, file_names in os.walk(path):
    print("The current folder is " + folder_name)
    for sub_folder in sub_folders:
        print("SUBFOLODER OF " + folder_name + ': ' + sub_folder)
    for file_name in file_names:
        print("FILE INSIDE " + folder_name + ": " + file_name)
    print('')

