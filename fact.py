n=int(input("enter the value:"))
r=int(input("enter the value:"))
fact_n=1
i=1
for i in range(1,n+1):
	fact_n=fact_n*i
print("factorial =",fact_n)

while(i<=r):
	fact_n=fact_n*i
	i=i+1
print("factorial =",fact_n)