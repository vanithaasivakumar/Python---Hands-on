#Lists,manipulating list items, slicing and nested lists

sample_list=[1,2,3,'one','two','three']
print(len(sample_list))     #6
print(sample_list[5])       #three
print(sample_list[-1])      #three
print(sample_list[1:])      #[2, 3, 'one', 'two', 'three']
print(sample_list[-1:])     #['three']
print(sample_list[:4])      #[1, 2, 3, 'one']
print(sample_list+['zero']) #[1, 2, 3, 'one', 'two', 'three', 'zero']
print(sample_list*2)        #[1, 2, 3, 'one', 'two', 'three', 1, 2, 3, 'one', 'two', 'three']

#LIST Methods
sample_list.append('end')
print(sample_list)          #[1, 2, 3, 'one', 'two', 'three', 'end']

print(sample_list.pop())    #end
print(sample_list.pop(3))   #one
print(sample_list)          #[1, 2, 3, 'two', 'three']

sample_list.reverse()
print(sample_list)          #['three', 'two', 3, 2, 1]

#sample_list.sort()         #TypeError: '<' not supported between instances of 'int' and 'str'
modified_list=['three','two','3','2','1','end']
modified_list.sort()
print(modified_list)        #['1', '2', '3', 'end', 'three', 'two']
modified_list.sort(reverse=True)
print(modified_list)        #['two', 'three', 'end', '3', '2', '1']

mylist=['name','address','name',100,'10']
print(mylist.count('name')) #2
print(mylist.count(2))      #0

#Difference between APPEND and EXTEND
sample_list.append(['item1','item2'])  #considers the whole items as a single element. Not Iterable
print(sample_list)                     #['three', 'two', 3, 2, 1, ['item1', 'item2']]
print(sample_list[5])                  #['item1', 'item2']
sample_list.extend(['e1','e2'])
print(sample_list)                     #['three', 'two', 3, 2, 1, ['item1', 'item2'], 'e1', 'e2']

print(sample_list.index("e2"))      #7
#print(sample_list.index(10))        #ValueError: 10 is not in list

sample_list.insert(2,'hello')
print(sample_list)                  #['three', 'two', 'hello', 3, 2, 1, ['item1', 'item2'], 'e1', 'e2']
sample_list.insert(15,'end')        #whatif the index value is more. value will be inserted at the end of the list
print(sample_list)                  #['three', 'two', 'hello', 3, 2, 1, ['item1', 'item2'], 'e1', 'e2', 'end']
print(sample_list.index('end'))     #9

sample_list.remove('end')
print(sample_list)                  #['three', 'two', 'hello', 3, 2, 1, ['item1', 'item2'], 'e1', 'e2']

sample_list.reverse()
print(sample_list)                  #['e2', 'e1', ['item1', 'item2'], 1, 2, 3, 'hello', 'two', 'three']

newlist=sample_list
print(newlist)                      #['e2', 'e1', ['item1', 'item2'], 1, 2, 3, 'hello', 'two', 'three']
newlist2=sample_list.append(5)
print(newlist2)                     #None
newlist3=newlist.copy()
newlist3.append(8)
print(newlist3)                     #['e2', 'e1', ['item1', 'item2'], 1, 2, 3, 'hello', 'two', 'three', 5, 8]

newlist3.clear()
print(newlist3)                     #[]













