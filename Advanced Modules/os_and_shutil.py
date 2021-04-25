import os

print(os.getcwd())
print(os.listdir())
print(os.listdir("C:\\Users"))

import shutil
#shutil.move("D:\\Python\\venv\\SampleText.txt","C:\\Users\\Vanitha")

for folder, sub_folders, files in os.walk("D:\\Python\\venv\\extracted_content"):
    '''
    print("Currently looking at folder: " + folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: " + sub_fold)

    print('\n')
    '''
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: " + f)
    print('\n')


