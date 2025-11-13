d = input().split()
nums = list(map(int, d))
for i in range(0, len(nums), 4):
    a1, a2, a3, a4 = nums[i:i+4]
    if a1 == a2 == a3 == a4 == 0:
        break
    cnt = 0
    while not (a1 == a2 == a3 == a4):
        b1 = abs(a1 - a2)
        b2 = abs(a2 - a3)
        b3 = abs(a3 - a4)
        b4 = abs(a4 - a1)
        a1, a2, a3, a4 = b1, b2, b3, b4
        cnt += 1
    print(cnt)