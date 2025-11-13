t = int(input())
for _ in range(t):
    s = list(map(float, input().split())) 

    maxs = max(s)
    mins = min(s)
    
    d = [x for x in s if x != maxs and x != mins]
    
    n = len(d)
    if n == 0:
        print(0) 
        continue
        
    b = sum(d)
    c = b / n
    print(round(c))