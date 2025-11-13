s = input().strip()
count = 0
while len(s) > 1:
    tong = 0
    for ch in s:
        tong += int(ch)
    s = str(tong)
    count += 1
print(count)
