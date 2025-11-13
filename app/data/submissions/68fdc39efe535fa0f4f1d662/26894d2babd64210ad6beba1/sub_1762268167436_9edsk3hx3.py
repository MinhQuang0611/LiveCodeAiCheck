t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    tudien = {}
    for i in a:
        tudien[i] = tudien.get(i, 0) + 1 
    found = False
    for k, v in tudien.items():
        if v > n / 2:
            print(k)    
            found = True
            break
    if not found:
        print("NO")    
