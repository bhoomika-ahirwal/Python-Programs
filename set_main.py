n=int(input("enter no. of items:"))
main_list=[ ]
for i in range(n):
	enter_item=int(input("enter item:"))
	main_list.append(enter_item)
print(main_list)
second_list=[ ]
for j in main_list:
	if j not in second_list:
		second_list.append(j)
print(second_list)