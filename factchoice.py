choice=True
while choice:
	n=int(input("enter n:"))
	fact=1
	for i in range (1,n+1):
		fact=fact*i
	print("factorial of {}={}".format(n,fact))
	user_choice=input("enter y to continue or n to stop")
	if user_choice=="n":
		choice=False
	else:
		choice=True