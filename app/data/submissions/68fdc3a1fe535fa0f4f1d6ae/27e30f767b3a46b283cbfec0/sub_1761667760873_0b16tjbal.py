def re_num(n):
    num = str(n)[::-1]
    return int(num)
t = int(input())
for _ in range(t):
    n = int(input())
    while n % 7 != 0:
        n += re_num(n)
    print(n)
