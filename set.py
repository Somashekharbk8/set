#creating set
set = {1,2,3,4,5}
print(type(set))
print(len(set))
print(set)

#set methods
#add
set1 = {1,2,3,4,5}
set1.add(16)#duplicate are not allowed
print(set1)#{1, 2, 3, 4, 5, 16}

#update

set2 = {1,3,5,7,9}
set2.update([1,2,3,4,5])
print(set2)#{1, 2, 3, 4, 5, 7, 9}

set3 = {1,2,3,4}
set4 = {5,6,7,8}
set3.update(set4)
print(set3)#{1, 2, 3, 4, 5, 6, 7, 8}

#remove

a = {1,2,3,4}
a.remove(4)
print(a)#{1, 2, 3}

#discard
b = {1,2,3,4}
b.discard(4)
print(a)#{1, 2, 3}

#pop

c = {1,2,3,4}
c.pop()#remove the index 0
print(c)#{2, 3, 4}

#copy
d = {1,2,3,4}
f=d.copy()
print(f)#{1, 2, 3, 4}

#clear
e = {1,2,3,4}
g=e.clear()
print(g)
























