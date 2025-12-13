user_input=input("enter sentence:")
article=("a","an","the")
words=user_input.split(" ")
article_count=0

for i in words:
	if i in article:
		article_count+=1
print("sentence:",user_input)
print("article_count:",article_count)
