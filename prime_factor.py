def primefactors(n):
	i = 2
	while(n > 1):
		if n % i == 0:
			factors.append(i)
			n = n // i
		else:
			i = i + 1
	return factors  

def represent(x):
	j = ""
	for i in x :
		if j == "":
			j = str(i)
		else : 
			j = j + "x" + str(i)

	return j 


n = int(input("Enter a number : "))
factors = [] 
result = represent(primefactors(n))
print("The prime factors of {} is : {}".format(n, result))

		

