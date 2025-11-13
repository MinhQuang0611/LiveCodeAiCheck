t = int(input())
for _ in range(t):
    s = input()
    result = ""
    so_luong = 1
    ky_tu = s[0]
    for i in range(1, len(s)):
        if s[i] == ky_tu:
            so_luong += 1
        else:
            result += str(so_luong) + ky_tu
            ky_tu = s[i]
            so_luong = 1
    result += str(so_luong) + ky_tu
    print(result)
