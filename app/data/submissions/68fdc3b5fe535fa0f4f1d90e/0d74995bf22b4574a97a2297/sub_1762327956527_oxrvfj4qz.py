def solve():
    n = input().strip()
    tich = 1
    tong = 0
    for i in range(len(n)):
        if i % 2 != 0 and i != 0:
            tich *= i
        else:
            tong += i
    print(tich, tong)
t = int(input())
for _ in range(t):
    solve()