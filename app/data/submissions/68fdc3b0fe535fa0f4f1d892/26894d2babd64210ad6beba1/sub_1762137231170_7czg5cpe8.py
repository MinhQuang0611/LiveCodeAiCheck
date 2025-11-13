t = int(input())

while(t>0):
    t-=1
    n = int(input())
    a = list(map(int, input().split()))
    tudien = {}
    for i in a:
        if i not in tudien:
            tudien[i] = 1
        else:
            tudien[i] += 1
    for i in tudien:
        if(tudien[i]%2!=0):
            print(i, " ")