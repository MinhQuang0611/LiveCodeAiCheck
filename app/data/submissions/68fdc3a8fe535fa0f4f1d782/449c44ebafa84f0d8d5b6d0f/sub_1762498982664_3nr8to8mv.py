n = input()
b = int(input())
a = []
for i in range(0, len(n) -1, 2):
    a.append(int(n[i:i+2]))
cnt = [0] * 100
for x in a:
    cnt[x] += 1
c = []
for x in a:
    if x not in c:
        c.append(x)
dem = 0
for x in c:
    print(x, cnt[x], end = ' ')
    print()
    if cnt[x] >= b:
        dem += 1
if dem == 0:
    print('NOT FOUND')