def check_prime(n):
    if n < 2:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1
n, m = map(int, input().split())
for _ in range(n):
    array = list(map(int,input().split()))
    for num in array:

        if check_prime(num):
            print(1,end = ' ')
        else:
            print(0,end = ' ')
    print()
