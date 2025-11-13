t = int(input())
for _ in range(t):
    n = int(input())
    nums = range(2 if n % 2 == 0 else 1,n+1,2)
    total = sum(1/x for x in nums)
    print(f"{total:.6f}")