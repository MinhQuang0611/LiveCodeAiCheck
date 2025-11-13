n = input()

a = []
for i in range(0, len(n)-1, 2):
    s = ""
    s = n[i] + n[i + 1]
    if s not in a:
        a.append(s)
print(*a)