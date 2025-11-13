a, b, c, d = map(int, input().split())
count=0
if a == 0 and b == 0 and c == 0 and d == 0:
    print(0)
while (a == b == c == d) == False:
    a,b,c,d= abs(a-b), abs(b-c), abs(c-d),abs(d-a)
    count+=1
print(count)