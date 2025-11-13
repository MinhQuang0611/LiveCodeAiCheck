n = int(input())
a = list(map(int, input().split()))
if max(a) == n:
    print('Excellent!')
else:
    for i in a:
        if a[i] - 1 != a[i - 1]:
            print(a[i] - 1)
            break