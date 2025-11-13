for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    kq = 0
    for i in a:
       kq ^= i
    print(kq)
