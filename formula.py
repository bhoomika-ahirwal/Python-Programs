print("Welcome to formula program")
print("Following formula are available ")
choice=int(input("Press 1 for (a-b)^2=a*2+b*2+(2*a*b),Press 2 for (a-b)^2=a*2+b*2-(2*a*b),Pres for 3 a*2-b*2=(a+b)(a-b) , Press for 4 (x+a)(x+b)=x*2+a*b , b*x,a*b:"))

if choice ==1:
	print("You have selected formula")
	a=int(input("Enter a"))
	b=int(input("Enter b"))
	result =(a*a)+(b*b)+(2*a*b)
	print(result)

if choice==2:
	print("You have selected formula")
	a=int(input("Enter a"))
	b=int(input("Enter b"))
	result =(a*a)+(b*b)-(2*a*b)
	print(result)

if choice==3:
	print("You have selected formula")
	a=int(input("Enter a"))
	b=int(input("Enter b"))
	result=(a+b)*(a-b)
	print(result)

if choice==4:
	print("You have selected formula")
	x=int(input("Enter x"))
	a=int(input("Enter a"))
	b=int(input("Enter b"))
	result=(x*x)+(a*x)+(b*x)+(a*b)
	print(result)
