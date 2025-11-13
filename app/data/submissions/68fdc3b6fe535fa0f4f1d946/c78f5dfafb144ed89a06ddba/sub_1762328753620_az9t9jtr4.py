a = input()
a=a.title()
c=""
for x in a:
    if x.isalnum() or x in [" ", ",", ":"]:
        c+=x
d=c.split()
print(" ".join(d))