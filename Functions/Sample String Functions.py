
def reverse_name(name):
    name_length=len(name)
    new_name=""
    while name_length>0:
        new_name+=name[name_length-1]
        name_length-=1
    return new_name

def check_palindrome(name):
    name2=reverse_name(name)
    if name==name2:
        print(name,"is a palindrome")
    else:
        print(name,"is not a palindrome")

def reverse_words_in_sentence(sentence):
    
    string_array=sentence.split()
    new_sentence=""
    length=len(string_array)
    i=0
    while length>0:
        new_sentence=new_sentence+reverse_name(string_array[i])+" "
        i+=1
        length-=1
    print(new_sentence)

   # new_sentence= ' '.join(sentence.split()[::-1])
    print(new_sentence)


check_palindrome("malayalam")
reverse_words_in_sentence("Hello world. My name is Vanitha")

'''
name="vanitha"
length=len("vanitha")
print(length)
print(name[5])
'''

