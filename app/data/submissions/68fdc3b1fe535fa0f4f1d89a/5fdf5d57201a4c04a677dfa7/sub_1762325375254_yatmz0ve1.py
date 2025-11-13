s = input()

solan = 0
while len(s) != 1:
    tong = 0
    for i in s:
        tong += int(i)
    s = str(tong)
    solan += 1

print(solan)