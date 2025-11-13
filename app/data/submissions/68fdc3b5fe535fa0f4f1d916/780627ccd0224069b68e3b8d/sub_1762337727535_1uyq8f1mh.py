n = int(input())
for i in range(n):
    s = input()
    b = []
    dem = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            dem += 1
        else:
            b.append(f"{dem}{s[i - 1]}")
            dem = 1
            
    b.append(f"{dem}{s[-1]}")
    print(''.join(b))