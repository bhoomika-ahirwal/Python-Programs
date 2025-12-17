var_x={2,3,4.5,6,6.3,"mohit",23}
for i in var_x:
	print(i)
print(var_x)
print(type(var_x))

#adding an item
var_x.add("bhoomika")
print(var_x)

#removing an item 
var_x.remove(2)
print(var_x)
var_x.discard(3)
print(var_x)

#removing non existing item using discard
var_x.discard(54)
print(var_x)