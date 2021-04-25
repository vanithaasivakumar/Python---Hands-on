student={1:"Alex",2:"Bob",3:"Charles",4:"David"}
print(student)                      #{1: 'Alex', 2: 'Bob', 3: 'Charles', 4: 'David'}
print(student.keys())               #dict_keys([1, 2, 3, 4])
print(student.values())             #dict_values(['Alex', 'Bob', 'Charles', 'David'])
print(student.items())              #dict_items([(1, 'Alex'), (2, 'Bob'), (3, 'Charles'), (4, 'David')])
first_student=student[1]
print(first_student)                #Alex

dict={'k1':123,'k2':['list','items'],'k3':{'newkey':'newdictionary'}}
print(dict['k3'])                   #{'newkey': 'newdictionary'}
print(dict['k3']['newkey'])         #newdictionary
print(dict['k2'][1])                #items
print(dict['k2'][1].upper())        #ITEMS

#Adding/overrriding the values in a key

dict['k4']=4.5
dict['k3']='update'
print(dict)                         #{'k1': 123, 'k2': ['list', 'items'], 'k3': 'update', 'k4': 4.5}



