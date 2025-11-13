n=int(input())
tong_uoc=0
if n <= 0:
    print('false')
else:    
    for i in range(1, n):
        if n % i == 0:
            tong_uoc+=i
    if tong_uoc == n:
        print('true')
    else:
        print('false')

