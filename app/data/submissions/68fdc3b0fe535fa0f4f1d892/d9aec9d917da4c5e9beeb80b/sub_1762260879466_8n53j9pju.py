n = int(input())
for i in range(n):
    b = int(input())
    a = list(map(int, input().split()))
    freq = 0
    for x in a:
        freq ^= x
    print(freq)
