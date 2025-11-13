def tich(n):
    tich = 1
    while n != 0:
        tich *= n % 10
        n //= 10
    return tich
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        n = list(map(int, input().split()))
        a = []
        for x in n:
            a.append([tich(x), x])
        a.sort( key = lambda x: (x[0], x[1]))
        for x in a:
            print(x[1], end = ' ')
        print()
