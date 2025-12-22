x=int(input("enter the value"))
for i in range(2,x):
	if x % i==0:
		for j in range(2,i):
			if x % j==0:
				print(i,"= Composite")
				break
		else:
			print(i,"= Prime")
	   
