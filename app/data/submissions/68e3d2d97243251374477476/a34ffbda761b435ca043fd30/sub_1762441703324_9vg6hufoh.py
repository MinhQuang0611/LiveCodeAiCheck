a = list(map(int, input().split()))
count = 0
if len(a)==1:
    if a[0]==1:
        count=1
    elif a[0]==0:
        count=0
for i in range(len(a)):
    if a[i] == 1:
        if a[i-1]==a[i]:
            count+=1
        else:
            count = 1
print(count)