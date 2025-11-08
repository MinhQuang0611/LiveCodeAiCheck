from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    l = Counter(list(map(int, input().split()))[:n])
    for (num, freq) in l.most_common():
        if freq != 2:
            print(num)