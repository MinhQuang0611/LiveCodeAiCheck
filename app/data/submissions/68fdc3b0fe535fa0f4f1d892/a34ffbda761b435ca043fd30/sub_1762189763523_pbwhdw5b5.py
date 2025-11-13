t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ket_qua=0
    for j in a:
        ket_qua ^= j
    print(ket_qua)
