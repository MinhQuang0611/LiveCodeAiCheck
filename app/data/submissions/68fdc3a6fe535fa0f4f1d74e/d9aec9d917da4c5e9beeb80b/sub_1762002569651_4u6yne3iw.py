t = int(input())
for i in range(t):
    nums = list(map(int, input().split()))
    valid = [num for num in nums if 1 <= len(str(num)) <= 8]
    valid.sort()
    total = sum(valid[:3])
    print(total)
