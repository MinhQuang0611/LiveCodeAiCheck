start, end = map(int, input().split())
chan = 0
le = 0
for n in range(start, end + 1):
    for ch in str(n):
        digit = int(ch)
        if digit % 2 == 0:
            chan += 1
        else:
            le += 1
print(chan, le)
