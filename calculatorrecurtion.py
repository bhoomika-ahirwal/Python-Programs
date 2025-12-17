def calculator():
	choice = int(input("Press 1 for Addition\nPress 2 for Substraction\nPress 3 for Multiplication\nPress 4 for Division\nEnter a Valid Choice : "))
	if choice==1:
		opr1=int(input("enter opr1:"))
		opr2=int(input("enter opr2:"))
		result=opr1+opr2
		print(result)
	elif choice==2:
		opr1=int(input("enter opr1:"))
		opr2=int(input("enter opr2:"))
		result=opr1-opr2
		print(result)
	elif choice==3:
		opr1=int(input("enter opr1:"))
		opr2=int(input("enter opr2:"))
		result=opr1*opr2
		print(result)
	elif choice==4:
		opr1=int(input("enter opr1:"))
		opr2=int(input("enter opr2:"))
		result=opr1/opr2
		print(result)
	else:
		print("invalid choice")
		
		calculator()
calculator()
