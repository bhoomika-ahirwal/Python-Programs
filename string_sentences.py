str1=input("enter sentence:")
con_str=""
flag=0
for i in range(len(str1)):
	if i == 0 or flag == 1:
		con_str = con_str + str1[i].upper()
		flag=0
	elif str1[i] == " ":
		con_str = con_str + str1[i]
		flag = 1
	else:
		con_str = con_str + str1[i].lower()
print("orignal string :",str1)
print("converted string :",con_str)
