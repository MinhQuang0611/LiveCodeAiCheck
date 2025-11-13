a = int(input())
so = []
while len(so) <a:
    so += list(map(int,input().split()))
thieu = []
for i in range(1,a+1):
    if i not in so:
        thieu.append(i)
if not thieu:
    print("Excellent!")
else:
    for x in thieu:
        print(x)
