n = int(input(""))
if n == 0:
    giaithua = 1
    print(giaithua)
elif n >=1:
    giaithua = 1
    for i in range(1,n+1):
     giaithua *= i
    print(giaithua)

