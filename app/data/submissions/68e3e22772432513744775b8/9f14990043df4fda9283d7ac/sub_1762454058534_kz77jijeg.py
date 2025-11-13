n = int(input())

if n < 0:
    print("Nhập lại số")
else:
    giaithua = 1
    for i in range(1, n+ 1):
        giaithua = giaithua*i
    print(giaithua)
