for _ in range(int(input())):
    t = int(input())
    nums = range(2 if t % 2 == 0 else 1,t+1,2)
    total = sum(1/x for x in nums)
    print(f"{total:.6f}")