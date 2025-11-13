n = int(input())
while n > 0:
    n-=1
    a=int(input())
    b=list(map(int, str(a)))
    true1 = sum(b)%10==0
    true2 = True
    for i in range(1, len(b)):
        if abs(b[i-1]-b[i])!=2:
            true2=False
            break
    if true1 and true2:
        print("YES")
    else:
        print("NO")