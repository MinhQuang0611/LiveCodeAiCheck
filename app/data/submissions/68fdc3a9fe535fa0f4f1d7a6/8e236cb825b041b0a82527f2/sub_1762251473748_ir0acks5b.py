t = int(input())
for _ in range(t):
    s = input()
    nums = []
    digits = []
    for c in s:
        if c.isdigit():
            digits.append(c)
        else:
            if len(digits) > 0:
                nums.append(int("".join(digits)))
                digits.clear()
    if len(digits) > 0:
        nums.append(int("".join(digits)))
    print(min(nums))
