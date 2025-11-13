def solve():
    s = input().strip()
    check = False
    tich = 1
    tong = 0
    for i in range(len(s)):
        d = int(s[i]) 
        if i % 2 == 0:
            if d != 0:
                tich *= d
                check = True
        else:
            tong += d
    if not check:
        tich = 0
    print(tich, tong)
t = int(input())
for _ in range(t):
    solve()
