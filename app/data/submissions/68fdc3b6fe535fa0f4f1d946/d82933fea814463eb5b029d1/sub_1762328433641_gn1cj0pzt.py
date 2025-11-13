a = str(input())
a = a.lower()
a = a.title()
b = ""
for i in a:
    if i.isalnum() or i in ",:":
        b += i
    else:
        b += " "
    
print(b)