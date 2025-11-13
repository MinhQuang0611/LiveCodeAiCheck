t = int(input())
for _ in range(t):
    s = input().strip()
    x = ''
    nums = []

    for ch in s:
        if ch.isdigit():
            x += ch
        else:
            if (x):
                nums.append(int(x))
                x = ''
    if (x):
        nums.append(int(x))

    print(min(nums) if nums else 0)

