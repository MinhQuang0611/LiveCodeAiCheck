n = int(input())
a = []
while len(a) < n:
    a += list(map(int, input().split()))
ln = max(a)
m = []
for i in range(1, ln + 1):
    if i not in a:
        m.append(i)
if not m:
    print("Excellent!")
else:
    for x in m:
        print(x) 