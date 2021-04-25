#1.Counter

from collections import Counter

mylist=[1,4,3,1,1,1,2,4,3,3,4,1,1,1,2,2,2,2,2]
cnt=Counter(mylist)
print(cnt)
print(cnt[2])

str='this is an additional function'
cnt2=Counter(str)
print(cnt2)
strlist=list(cnt2.elements())
print(strlist)
print(list(cnt.elements()))
print(cnt.most_common())
print(cnt.most_common(2))

cnt3 = Counter({1:3,2:4,3:3})
deduct = {1:1, 2:2}
cnt3.subtract(deduct)
print(cnt3)

#2.defaultdict

from collections import defaultdict

mydict=defaultdict(int)
mydict[1]='one'
mydict[2]='two'
mydict[3]='three'
print(mydict)
print(mydict[4])

count = defaultdict(int)
names_list = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
for names in names_list:
    count[names] +=1
print(count)

from collections import OrderedDict
mylist=[1,4,3,1,1,1,2,4,3,3,4,1,1,1,2,2,2,2,2]
cnt4=Counter(mylist)  #Counter({1: 7, 2: 6, 4: 3, 3: 3})
d=dict(cnt4.most_common())    #{1: 7, 2: 6, 4: 3, 3: 3}
od=OrderedDict(cnt4.most_common())   #OrderedDict([(1, 7), (2, 6), (4, 3), (3, 3)])
print(cnt4)
print(d)
print(od)

#3.deque
from collections import deque

list = ["a","b","c"]
deq = deque(list)
print(deq)

deq.append("d")
deq.appendleft("e")
print(deq)

deq.pop()
deq.popleft()
print(deq)

list = ["a","b","c"]
deq = deque(list)
print(deq.count("a"))

#4.ChainMap
from collections import ChainMap

dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)
print(chain_map.maps)
print(chain_map['b'])

dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)


dict3 = {'e' : 5, 'f' : 6}
new_chain_map = chain_map.new_child(dict3)
print(new_chain_map)

#5.namedtuple
from collections import namedtuple
Student = namedtuple('Student', 'fname, lname, age')
s1 = Student('John', 'Clarke', '13')
print(s1.fname)