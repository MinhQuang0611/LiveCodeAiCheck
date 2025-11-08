n = int(input())
for i in range(n):
    a = input().strip()
    for s in range(len(a)-1):
        if a[s] <= a[s+1]: 
            print("YES")
            break
        else: 
            print("NO")
            break
   