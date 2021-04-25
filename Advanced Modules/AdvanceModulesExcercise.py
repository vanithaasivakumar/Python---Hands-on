import os
print(os.getcwd())
'''
import zipfile
file=zipfile.ZipFile("C:\\Users\\Vanitha\\Downloads\\unzip_me_for_instructions.zip","r")
    file.extractall("D:\\Python\\venv") '''

import re
pattern=r"\d{3}-\d{3}-\d{4}"
phone=[]
for folders,subfolders,files in os.walk("D:\\Python\\venv\\extracted_content"):
    for f in files:
        fullpath=folders+"\\"+f
        with open(fullpath,"r") as openedfile:
            text=openedfile.read()
            match=re.findall(pattern,text)
            if match!=[]:
                phone.extend(match)
print(phone[0])


