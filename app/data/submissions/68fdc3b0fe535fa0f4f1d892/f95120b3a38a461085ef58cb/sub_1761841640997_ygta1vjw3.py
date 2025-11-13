t = int(input())
for _ in range(t):
    n = int(input())
    da = list(map(int, input().split()))
    result = 0
    for number in da:
        result ^= number  
    print(result)  