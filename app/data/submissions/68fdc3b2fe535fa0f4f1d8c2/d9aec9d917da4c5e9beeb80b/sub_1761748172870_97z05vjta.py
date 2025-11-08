n = int(input())
a = list(map(int, input().split()))

a.sort()  

miss = 1 
for x in a:
    if x == miss:
        miss += 1
print(miss)