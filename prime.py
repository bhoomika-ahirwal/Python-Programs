x=int(input("enter value:"))
for i in range (2,x):
	if x % i==0:
		print("composite")
		break
else:
	print("prime")