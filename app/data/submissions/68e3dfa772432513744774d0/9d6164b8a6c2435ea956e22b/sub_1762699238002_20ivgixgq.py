n = list(map(int, input().split()))
b = list(set(n))                 
b.sort()             
if len(b) >= 3:
    print(b[-3])                  
else:
    print(None)