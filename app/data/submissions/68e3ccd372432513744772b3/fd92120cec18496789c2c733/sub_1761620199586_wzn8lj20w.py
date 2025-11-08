start,end = map(int,input().split())
a = 0
b = 1
total = 0
while b <= end :
    if b >= start and b % 2 == 0:
        total += b
    a,b = b,a+b
print (total)