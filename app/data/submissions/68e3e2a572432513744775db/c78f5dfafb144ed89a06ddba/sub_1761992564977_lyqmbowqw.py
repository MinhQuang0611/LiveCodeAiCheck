n = list(map(int, input().split()))
if n == []:
    print(float(0))
else:
    tong = sum(n)
    average = tong/len(n)
    print(average)