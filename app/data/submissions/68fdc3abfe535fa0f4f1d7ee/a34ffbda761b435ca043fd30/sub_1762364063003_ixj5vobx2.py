t = int(input())
for i in range(t):
    n = int(input())
    tong=0
    if n%2==0:
        for j in range(2, n+1, 2):
            tong+=1/j
    else:
        for j in range(1, n+1, 2):
            tong+=1/j
    print(f"{tong:.6f}")