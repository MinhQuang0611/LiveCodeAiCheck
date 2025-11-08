n=int(input())
a=list(map(float,input().split()))
a.sort()
b=a[1:-1]
if len(a) == 0 :
    print("0.00")
else:
    tong=sum(b)/len(b)
    print(f"{tong:.2f}")
