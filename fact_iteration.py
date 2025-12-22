def fact(x):
	if x==0 or x==1:
		return 1
	else:
		return x * fact(x-1)

n=int(input("enter the value:"))
m=int(input("enter the value:"))
fact_n=1
result=fact(n)
for i in range(m,0,-1):
	fact_n=fact_n*i  
print(fact_n)
print(result)