s = input().strip()
n = len(s)

a = []
while n > 3:
    a.append(s[n-3:n])
    n -= 3
a.append(s[:n])

print(','.join(a[::-1]))
