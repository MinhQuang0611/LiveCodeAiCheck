n = int(input())
a = list(map(int, input().split()))
a.sort()
if a[0] + len(a) - 1 == a[-1]:
    print('Excellent!')
else:
    for i in range(len(a) - 1):
        if a[i] + 1 < a[i + 1]:
            for j in range(a[i] + 1, a[i + 1]):
                print(j, end = ' ')

    
            