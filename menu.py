print("Welcome to Bhoomika's Cafe")

billing_amount = 0
next_choice = True
while next_choice :
choice=int(input("press 1 for samosa\npress 2 for tea\npress 3 for coffee\npress 4 for colddrink\nenter a valid choice:"))
if choice == 1:
	quantity = int(input("enter no. of samosa : "))
	price = 10
	amount = quantity*price
elif choice == 2:
	quantity = int(input("enter no. of tea :"))
	price = 5:
	amount = quantity*price
elif choice == 3:
	quantity = int(input("enter no. of coffee :"))
	price = 20:
	amount = quantity*price
elif choice == 4:
	quantity = int(input("enter no. of colddrink :"))
	price = 20
	amount = quantity*price
else :
	print("invalid Item")
billing_amount = billing_amount + billing_amount
next_item = input("enter y to add other item or any other key to stop")
if next_item == "y" or next_item == "Y":
	next_choice = True 
else:
	next_choice 


    
