numbers=[]
n=int(input("enter value:"))
for i in range(n):
	item=int(input("enter value:"))
	numbers.append(item)
print(numbers)
sum=0
for j in numbers:
	sum=sum+j
average=sum/n
print("average of {}={}".format(numbers,average))