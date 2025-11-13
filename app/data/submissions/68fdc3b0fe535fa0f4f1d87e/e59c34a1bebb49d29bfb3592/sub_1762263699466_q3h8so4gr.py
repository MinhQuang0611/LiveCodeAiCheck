a = int(input())
c = list(map(int, input().split()))
b = []

for i in range(a):
    if not b:  
        b.append(c[i])
    else:
        if (c[i] + b[-1]) % 2 != 0:
            b.append(c[i])
        else:  
            b.pop()

print(len(b))
