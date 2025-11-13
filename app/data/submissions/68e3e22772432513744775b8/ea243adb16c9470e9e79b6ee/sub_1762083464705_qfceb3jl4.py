n = int(input())
gthua = 1
if n >= 0:
    if n <= 1:
        print(1)
    else:
        for i  in range(2, n + 1):
            gthua = gthua * i
        print(gthua)
else:
    print('error')
