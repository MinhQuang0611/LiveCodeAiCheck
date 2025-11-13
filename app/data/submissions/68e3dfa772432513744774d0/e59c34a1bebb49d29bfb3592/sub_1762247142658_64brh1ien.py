arr = list(map(int,input().split()))
n = sorted(set(arr),reverse = True)
if len(n) >= 3:
    print(n[2])
else:
    print(n[0])