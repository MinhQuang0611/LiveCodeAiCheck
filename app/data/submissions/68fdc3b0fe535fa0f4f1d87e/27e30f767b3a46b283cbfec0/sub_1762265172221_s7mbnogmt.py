n = int(input())
a = list(map(int,input().split()))
b = []
for i in range(n):
    if a[i] not in b:
        b.append(a[i])
    elif a[i] + b % 2 == 0:
        b.pop()
    elif a[i] + b % 2 != 0:
        b.append(a[i])
print(len(b))

