n = int(input())
db = [0]*n
for i in range(0,n):
    db[i] = input()
sl = n


def test(a):
    sl = len(a)
    for i in range(2,sl):
        if i % 2 == 0:
            if a[i] != a[0]:
                return print("NO")
        else:
            if a[i] != a[1]:
                return print("NO")
    return print("YES")


for i in range(0,sl):
    test(db[i])

