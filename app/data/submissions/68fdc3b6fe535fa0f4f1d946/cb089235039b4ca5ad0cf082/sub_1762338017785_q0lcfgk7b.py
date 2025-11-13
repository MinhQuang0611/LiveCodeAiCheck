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
D = ' '.join(b)
for k in c:
    D = D.replace(k, ' ')
D = ' '.join(D.split())
print(D)