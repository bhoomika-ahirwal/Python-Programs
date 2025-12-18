'''a=1
for i in range(1,1+n):
	a=a*i   
	print("factorial of {}={}".format(n,a))'''
n=int(input("enter value:"))
a=1
for i in range(n,0,-1):
	a=a*i  
	print(a)
	n=int(input("enter the value"))
