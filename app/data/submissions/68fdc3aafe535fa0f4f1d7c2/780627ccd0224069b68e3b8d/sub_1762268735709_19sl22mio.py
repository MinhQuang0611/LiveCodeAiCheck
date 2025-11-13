s = input()
a = []
for i in  range(1, len(s), 2):
    tmp = s[i-1] + s[i]
    a.append(int(tmp))
b = list(set(a))
b.sort()
for i in b:
    print(i, end = ' ')