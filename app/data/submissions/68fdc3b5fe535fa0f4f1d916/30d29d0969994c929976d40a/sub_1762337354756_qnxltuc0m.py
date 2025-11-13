t = int(input())
for _ in range(t):
    s = input()
    kq = []
    dem = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            dem += 1
        else:
            kq.append(f"{dem}{s[i-1]}")
            dem = 1
    kq.append(f"{dem}{s[-1]}") 
    print("".join(kq))
