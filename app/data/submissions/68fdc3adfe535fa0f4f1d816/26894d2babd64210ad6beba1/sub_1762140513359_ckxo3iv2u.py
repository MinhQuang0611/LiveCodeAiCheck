t = int(input())

while(t>0):
    t-=1
    a, x, b = map(int,input().split())
    i = 0
    while a < b:
        i += 1
        a += a * x /100
    print(i)