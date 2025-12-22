def check_prime(x):
	for i in range(2,x):
		if x% i == 0:
			return True
	else:
		return False
n=int(input("enter value:"))
factor=[ ]
for i in range(2,n):
	if n % i == 0:
		factor.append(i)
prime_factor=[ ]
composite_factor=[ ]
for m in factor:
	result=check_prime(m)
	if result==True:
		composite_factor.append(m)
	else:
		prime_factor.append(m)
print("factor:",factor)
print("prime factor:",prime_factor)
print("composite factor:",composite_factor)