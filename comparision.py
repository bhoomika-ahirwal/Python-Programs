a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))
d=int(input("enter the value of d:"))
if a>b and a>c and a>d:
	print("a is greatest")
elif b>a and b>c and b>d:
	print("b is greatest")
elif c>a and c>b and c>d:
	print("c is greatest")
else:
	print("d is greatest")
