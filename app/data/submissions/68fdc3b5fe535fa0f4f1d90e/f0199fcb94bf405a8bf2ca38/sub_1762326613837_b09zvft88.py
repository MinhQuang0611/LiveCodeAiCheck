t = int(input())
for k in range(t):
    n = input()
    tich = 1
    tong = 0
    for i in range(len(n)):
        if i % 2 == 0:
            temp = int(n[i])
            tich = tich * temp
        else:
            temp = int(n[i])
            tong = tong + temp
    print(tich,tong)