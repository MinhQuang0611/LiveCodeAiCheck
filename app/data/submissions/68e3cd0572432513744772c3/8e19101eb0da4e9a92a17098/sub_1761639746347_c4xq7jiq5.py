n = int(input())
s = str(n)
f = 'false'
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        f = 'true'
        break
print(f)