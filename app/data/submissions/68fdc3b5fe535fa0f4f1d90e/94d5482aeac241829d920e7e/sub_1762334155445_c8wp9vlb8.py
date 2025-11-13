t = int(input())
while(t > 0):
    t -= 1
    s = input()
    s = '*' + s
    tong = 0
    tich = 1
    for i in range(1,len(s)):
        if(i % 2 == 1): tich *= int(s[i])
        else: tong += int(s[i])
    print(tich, tong)
