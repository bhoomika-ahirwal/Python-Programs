p1=int(input("enter 1 for rock,enter 2 for paper,enter 3 for scissor,enter choise:"))
p2=int(input("enter 1 for rock,enter 2 for paper,enter 3 for scissor,enter choise:"))
if p1==p2:
	print("its a tie")
elif p1==1 and p2==2:
	print("p2 win")
elif p1==1 and p2==3:
	print("p1 win")
elif p1==2 and p2==1:
	print("p1 win")
elif p1==2 and p2==3:
	print("p2 win")
elif p1==3 and p2==1:
	print("p1 win")
elif p1==3 and p2==2:
	print("p1 win")