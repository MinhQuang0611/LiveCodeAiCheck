a = input()
b = a.lower()
c = ["a","e","i","o","u"]
d = 0
for i in b:
    if i in c:
        d+=1
print(d)