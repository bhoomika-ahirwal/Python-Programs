n=int(input("enter the value of n:"))
r=int(input("enter the value of r:"))
fact_n=1
for i in range(1,n+1):
	fact_n=fact_n*i
fact_nr=1
for j in range(1,(n-r)+1):
	fact_nr=fact_nr*j
fact_r=1
for k in range(1,(r+1)):
	fact_r=fact_r*k
ncr=fact_n/(fact_r*fact_nr)
print("{}c{}={}".format(n,r,ncr))
