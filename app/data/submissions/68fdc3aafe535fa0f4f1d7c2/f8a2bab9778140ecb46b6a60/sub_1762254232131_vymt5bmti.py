n = input()
a = []
for i in range(0,len(n),2):
    if n[i:i+2] not in a: 
        a.append(n[i:i+2])
b = " ".join(a)
print(b)
