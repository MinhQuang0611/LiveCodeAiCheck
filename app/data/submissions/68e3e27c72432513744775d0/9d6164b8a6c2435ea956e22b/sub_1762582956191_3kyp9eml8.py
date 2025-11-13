n = int(input())
if n < 0:
    print ("không phải số tự nhiên")
else:
    tong = 0
    for i in range(1, n+1):
        tong += i
    print (tong) 