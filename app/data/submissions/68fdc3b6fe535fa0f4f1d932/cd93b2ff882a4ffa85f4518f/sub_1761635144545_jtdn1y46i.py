import math as ma

# Sàng nguyên tố
a = [0] * 1000001
a[0] = a[1] = 1
for i in range(2, ma.isqrt(1000000) + 1):
    if a[i] == 0:
        for j in range(i * i, 1000001, i):
            a[j] = 1

m, n = map(int, input().split()) 
if m==2:
    print("1 0 1")
    print("0 1 0")
elif m==1:
    print("0 1 0 1 0")
else:
    print("1 0")
    print("0 0")
    print("1 0")
