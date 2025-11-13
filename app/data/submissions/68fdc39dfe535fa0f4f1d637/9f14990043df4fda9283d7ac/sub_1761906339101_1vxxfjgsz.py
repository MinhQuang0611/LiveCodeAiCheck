t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    
    if all(A[i] <= B[i] for i in range(n)):
        print("YES")
    else:
        print("NO")
