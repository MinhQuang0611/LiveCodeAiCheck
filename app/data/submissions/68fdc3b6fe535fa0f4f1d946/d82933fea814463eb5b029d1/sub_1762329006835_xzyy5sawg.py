a = str(input()).lower().title()
b = ""
for i in a:
    if i.isalnum() or i in ',:':
        b += i
    elif i.isspace():
        b += " "
    else:
        b += ""
print(b)