n = int(input(''))
a = []
count = 0
while count < n:
    line = input()
    b = line.split()
    for i in b:
        if count<n:
            a.append(float(i))
            count+=1
        else:
            break
c = []
m2 = max(a)
for j in range(1, int(m2)+1):
    c.append(j)
miss_list = []
for k in c:
    if k not in a:
        miss_list.append(k)

if miss_list == []:
    print("Excellent!")
else:
    for m in miss_list:
        print(m)
    print()