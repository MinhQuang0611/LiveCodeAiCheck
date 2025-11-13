def so_sanh(n,a,b):
    if all(i<=j for i,j in zip(a,b)): #zip(a,b) dùng để ghép từng phần tử tương ứng
        print("YES")
    else: print("NO")
t=int(input())
for _ in range(t):
    n = int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    so_sanh(n,a,b)