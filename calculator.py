def add():
	x = int(input("Enter Operand 1 : "))
	y = int(input("Enter Operand 2 : "))
	z = x + y
	print("{} + {} = {}".format(x,y,z))

def sub():
	x = int(input("Enter Operand 1 : "))
	y = int(input("Enter Operand 2 : "))
	z = x - y
	print("{} - {} = {}".format(x,y,z))

def mul():
	x = int(input("Enter Operand 1 : "))
	y = int(input("Enter Operand 2 : "))
	z = x * y
	print("{} * {} = {}".format(x,y,z))

def div():
	x = int(input("Enter Operand 1 : "))
	y = int(input("Enter Operand 2 : "))
	z = x / y
	print("{} / {} = {}".format(x,y,z))

choice = int(input("Press 1 for Addition\nPress 2 for Substraction\nPress 3 for Multiplication\nPress 4 for Division\nEnter a Valid Choice : "))
if choice == 1 :
	add()
elif choice == 2 :
	sub()
elif choice == 3 :
	mul()
elif choice == 4 :
	div()
else :
	print("Invalid Choice")
