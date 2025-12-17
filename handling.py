a="Bhoomika"
b=""
for i in range(len(a)):
	if i % 2 == 0:
		x=a[i].lower()
		b=b+x
	else:
		x=a[i].upper()
		b=b+x
print(a)
print(b)
