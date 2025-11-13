n = int(input())
a = list(map(int, input().split()))
lon = max(a)
be = min(a)
summ = []
for i in a:
    if i != lon and i != be:
        summ.append(i)
print(sum(summ)//len(summ))