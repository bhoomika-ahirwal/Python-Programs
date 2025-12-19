var_1=["bhoomika",18,65,"indore"]
print(var_1)
print(type(var_1))
#read
for i in range (len(var_1)):
	print(i)
	print(var_1[i])
#itratable
for j in var_1:
	print(j)
#adding item at last
var_1.append("raikwar")
print(var_1)
#adding item at specific index
var_1.insert(2,"tony")
print(var_1)
#changing an element
item=18
x=var_1.index(item)
var_1[x]=20
print(var_1)
#remove an item
var_1.pop()
var_1.remove(20)
print(var_1)