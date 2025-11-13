t = int(input())

group = set([])
while(t>0):
    t-=1
    a, b, c = map(int, input().split())
    if(c == 1):
        group.add(a)
        group.add(b)
    else:
        if(a not in group or b not in group):
            print(0)
        else:
            print(1)
