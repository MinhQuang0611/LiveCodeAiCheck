t = int(input())
for i in range(t):
    n = input()
    a = 1
    b = 0
    co_so_khong=False
    for i in range(len(n)):
        digit= int(n[i])
        if i%2==0:
            if digit != 0:
                    a *= digit
            else:
                a= 0
        else:
            b += digit
    print(f"{a} {b}")