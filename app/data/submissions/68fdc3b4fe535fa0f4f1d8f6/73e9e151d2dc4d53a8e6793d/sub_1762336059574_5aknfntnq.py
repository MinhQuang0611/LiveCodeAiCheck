a = list(map(int, input().split()))
count = 0
while True:
    if a[0] == a[1] == a[2] == a[3] == 0:
        break
    a = [abs(a[i] - a[(i + 1) % 4]) for i in range(4)]
    count += 1
print(count-1)