n = int(input())
a = []
count = 0
while count < n:
    line = float(input())
    b = line.split()
    for i in b:
        if count<n:
            a.append(i)
            count+=1
        else:
            break
s=0
for i in a:
    s+=i
print(s/len(a))
