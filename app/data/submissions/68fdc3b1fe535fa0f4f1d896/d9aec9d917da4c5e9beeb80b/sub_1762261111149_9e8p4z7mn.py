t = int(input())
for i in range(t):
    n = int(input())
    if n < 2:
        print("NO")
    else:
        ok = True
        for i in range(2, n+1, 1):

            if n % i == 0:
                ok = False
                break
        if ok:
            print("YES")
        else:
            print("NO")

