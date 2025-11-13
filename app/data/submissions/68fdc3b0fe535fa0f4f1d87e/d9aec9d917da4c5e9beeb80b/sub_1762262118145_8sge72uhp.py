n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    if not b:
        b.append(i)
    else:
        if (i + b[-1]) % 2 == 0:
            b.pop()
        else:
            b.append(i)
print(len(b))