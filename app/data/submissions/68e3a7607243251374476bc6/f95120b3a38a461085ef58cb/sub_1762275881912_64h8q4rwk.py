def check(nums):
    cnt = 0
    string = str(nums)

    for ch in string:
        if ch == "1":
            cnt += 1
    return cnt
nums = int(input())
cnt = 0
for i in range(1, nums + 1):
    cnt += check(i)
print(cnt)