s = input().strip()
a = s[::-1]
b = [a[i:i+3]for i in range(0, len(a), 3)]
r = ",".join(b)
q = r[::-1]
print(q)
