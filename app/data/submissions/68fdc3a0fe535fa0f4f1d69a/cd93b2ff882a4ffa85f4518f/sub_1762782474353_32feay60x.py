m=int(input())
for _ in range (m):
    n = int(input())
    mo=[]
    for _ in range(n):
        a, b = map(int, input().split())
        mo.append((a, b))
    mo.sort(key=lambda x: x[1])
    count=0
    end=0
    for a, b in mo:
        if a >= end:  
            count += 1
            end= b   
    print(count)