n = input()
n = n.replace("-", "")
tong = 0
for ch in n:
    tong += int(ch)
print(tong)