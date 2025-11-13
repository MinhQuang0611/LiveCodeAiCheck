s = input()
a = s.lower()
b = []
a = a.split(' ')
c = [".", "?", "!","&"]
for i in a:
    if i:
        b.append(i.capitalize())
    else:
        b.append(i) 
d = ' '.join(b)
for k in c:
    d = d.replace(k, ' ')
d = ' '.join(d.split())
print(d)