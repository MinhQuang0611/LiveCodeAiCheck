a = input()
a=a.title()
c=""
for x in a:
    if x.isalnum() or x in [" ", ",", ":"]:
        c+=x
    elif x == "!":
        c += "\n"
print(c.replace("\n ", "\n"))