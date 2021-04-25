myfile=open('SampleText.txt')
print(myfile.read())   #displays file content
print(myfile.read())    #running it again will display empty string. Cursor is in end of the file
myfile.seek(0)          #brings the cursor to the beginning of the file
print(myfile.read())
myfile.seek(0)
print(myfile.readlines()) #['Hello World\n', 'Good Day!\n'] Creates a List of lines as elements
myfile.close()
myfile2=open('‪D:\\Python\\Sample files\\SampleText.txt')   #'/' is used in Mac and linux
myfile2.close()
with open('SampleText.txt') as no_close_file:
    contents=no_close_file.read()
    print(contents)






#myfile2=open('NotExistFile.txt')