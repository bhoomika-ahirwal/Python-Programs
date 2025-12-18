def fact(x):
	if x==0 or x==1:
		return 1
	else:
		return x * fact(x-1)

n=int(input("enter the value:"))
result=fact(n)
print("factorial of {}={}".format(n,result))



