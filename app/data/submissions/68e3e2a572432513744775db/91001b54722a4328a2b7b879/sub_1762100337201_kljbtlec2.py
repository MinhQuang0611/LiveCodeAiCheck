s = list(map(float, input().split()))
if len(s) == 0:
    print(0.0)
else: 
    tbc = sum(s) / len(s)
    print(tbc)