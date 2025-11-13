n = input()
db = n.split()
sl = int(db[0])

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


for i in range(1,sl+1):
    test(db[i])


