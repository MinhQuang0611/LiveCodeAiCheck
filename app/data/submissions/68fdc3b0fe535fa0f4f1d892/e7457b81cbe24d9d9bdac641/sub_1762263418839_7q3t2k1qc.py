n=int(input())
for _ in range(n):
    n = int(input()) 
    a = list(map(int, input().split()))
    so = 0
    for x in a:
        so ^= x  
    print(so)