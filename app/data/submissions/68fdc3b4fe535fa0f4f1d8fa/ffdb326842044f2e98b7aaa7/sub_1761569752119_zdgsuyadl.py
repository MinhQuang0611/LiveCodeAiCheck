def check(n):
    if n < 2: return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False

    return True

n = int(input())
lst = list(map(int, input().split()))

isprime = []

for index, nums in enumerate(lst):
    if check(nums):
        isprime.append(nums)

isprime.sort()

start = 0
end = len(isprime)

for index, nums in enumerate(lst):
    if check(nums) and start < end:
        print(isprime[start], end = " ")
        start += 1
    else:
        print(nums, end = " ")

