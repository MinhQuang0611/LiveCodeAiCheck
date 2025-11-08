s = input()
so = s.strip('[]').split(',')
f = [int(i) for i in so]
for i in range(len(f)):
    f[i] = f[i] ** 2
s = str(f).replace(" ", "")
print(s)