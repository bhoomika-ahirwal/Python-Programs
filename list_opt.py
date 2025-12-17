# Create
list1 = ["Rajvi","Sunny","Kirtan","Girish"]
print(list1)
print(type(list1))
print(len(list1))

#read

for i in range(len(list1)):
	print(i)
	print(list1[i])

for j in list1:
	print(j)

#udate
#addind an element at last index
list1.append("Bhoomika")
print(list1)

#adding an element at specific index
list1.insert(2,"Adarsh")
print(list1)

#know index of a given value
print(list1.index("Bhoomika"))

#change the element
list1[1] = "Harsh"
print(list1)

#deleting a item 
list1.pop()
print(list1)

list1.remove("Kirtan")
print(list1)
