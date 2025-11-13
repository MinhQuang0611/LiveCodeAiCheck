a = list(map(int, input().split()))
b = False
for i in a:
    if a.count(i)>len(a)//2:
        c = i
print(c)