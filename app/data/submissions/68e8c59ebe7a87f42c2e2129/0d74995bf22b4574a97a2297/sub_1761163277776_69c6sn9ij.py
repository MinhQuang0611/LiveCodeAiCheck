n = float(input())
if(n <= 1):
    print(10000)
elif(1 < n <= 10):
    print(int(10000 + (n - 1)* 8500))
else:
    print(int(10000 + 9 * 8500 + (n - 10)*7500))