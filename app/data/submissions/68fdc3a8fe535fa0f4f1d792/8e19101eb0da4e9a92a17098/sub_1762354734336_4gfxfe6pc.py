t = int(input())
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(t):
    n, k = map(int, input().split())
    if n == 0:
        print("0")
        continue
    ans = ""
    while n > 0:
        r = n % k
        ans = digits[r] + ans
        n //= k
    print(ans)
