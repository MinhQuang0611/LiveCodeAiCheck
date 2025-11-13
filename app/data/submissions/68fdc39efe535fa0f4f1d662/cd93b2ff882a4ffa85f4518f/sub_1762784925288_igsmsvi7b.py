t=int(input())
for _ in range (t):
    n=int(input())
    a=[int(x) for x in input().split()]
    check=[0]*(max(a)+1)
    for x in a:
        check[x]+=1
    k=n//2 if n%2==0 else n//2 + 1
    found=False
    for i in range(len(check)):
        if check[i]>=k:
            print(i)
            found=True
            break
    if not found:
        print("NO")
