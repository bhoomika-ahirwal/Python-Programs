 /ebilling_amount = 0
next_choice = True
billing amount
while next_choice :

choice=int(input("press 1 for chips\npress 2 for coke\npress 3 for chocolate\nenter a valid choice "))
if choice==1:
	quantity=int(input("enter no. of chips:"))
	rate=10
	amout=quantity*rate
	print(amount)
elif choice==2:
	quantity=int(input("enter no. of coke:"))
	rate=10
	amout=quantity*rate
elif choice==3:
	quantity=int(input("enter no. of chocolate:"))
	rate=10
	amout=quantity*rate
else:
	print(invalid)

billing_amount = billing_amount + billing_amount
next_item = input("enter y to add other item or any other key to stop")
if next_item == "y" or next_item == "Y":
	next_choice = True
