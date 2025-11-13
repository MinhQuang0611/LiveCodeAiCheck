a = int(input())
for i in range(a):
    m, n= map(int, input().split())
    import math
    ucln = math.gcd(m, n)
    h = sum(int(digit) for digit in str(ucln))
    ket_qua = True
    if h == 1:
        ket_qua = False
    for l in range(2, int(h**0.5)+1):
        if h%l==0:
            ket_qua=False
    if ket_qua:
        print("YES")
    else:
        print("NO")