def nguoc(n):
    res = 0
    while n != 0:
        res = res * 10 + n % 10
        n //= 10
    return res 
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n % 7 == 0:
            print(n)
        else:
            while n % 7 != 0:
                n = n + nguoc(n)
            print(n)
