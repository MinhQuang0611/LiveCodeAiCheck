s = input().strip()
t = s[::-1]


p = [t[i:i+3] for i in range(0, len(t), 3)]


ans = ','.join(p)[::-1]

print(ans)
