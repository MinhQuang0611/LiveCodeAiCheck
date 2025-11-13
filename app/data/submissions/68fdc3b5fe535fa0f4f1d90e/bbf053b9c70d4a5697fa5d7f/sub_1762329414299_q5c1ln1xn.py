t = int(input())
for i in range(t):
    s = input().strip()
    x = 1
    a = 0
    b = False
    for i in range(len(s)):
        so = int(s[i])
        if (i + 1) % 2 == 1:
            if so != 0:
                x *= so
                b = True
        else:
            a += so
    if not b :
        x = 0
    print(x, a)