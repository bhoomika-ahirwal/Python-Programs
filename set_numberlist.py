n=int(input("enter the repitations"))
list_1=[]
for i in range(n):
	x=int(input("enter the value:"))
	list_1.append(x)
print(list_1)
list_2=list(set(list_1))
print(list_2)