n=int(input())
for i in range (0,n):
    k=0
    s=input()
    for ch in s:
        if ch not in '47':
            k=1
            break
    if k==0:
        print("YES")
    else:
        print("NO")
    