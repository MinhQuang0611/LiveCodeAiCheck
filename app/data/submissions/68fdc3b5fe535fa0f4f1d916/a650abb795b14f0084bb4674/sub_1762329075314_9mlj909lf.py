t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    kq = ""
    count = 1

    for i in range(1, n):
        if s[i] == s[i-1]:
            count = count + 1
        else:
            kq = kq + str(count) + s[i-1]
            count = 1

    kq = kq + str(count) + s[n-1]
    print(kq)
    