t = int(input())
s = input().strip()
kq = ""
count = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        kq += str(count) + s[i - 1]
        count = 1
kq += str(count) + s[-1]
print(kq)