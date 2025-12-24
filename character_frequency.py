s = input("Enter a string: ")

for ch in s:
    if s.count(ch) > 0:
        print(ch, ":", s.count(ch))
        s = s.replace(ch, "")