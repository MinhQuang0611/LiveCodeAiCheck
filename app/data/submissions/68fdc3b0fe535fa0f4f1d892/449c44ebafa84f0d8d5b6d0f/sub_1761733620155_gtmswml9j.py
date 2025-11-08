if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        cnt = [0] * ( 10 ^ 6 )
        for x in a:
            cnt[x] += 1
        for x in a:
            if cnt[x] % 2 != 0:
                print(x)
                break