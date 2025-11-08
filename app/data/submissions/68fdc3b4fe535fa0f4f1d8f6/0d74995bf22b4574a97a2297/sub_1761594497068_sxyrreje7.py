import sys
input = sys.stdin.readline
while True:
    a, b, c, d = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0:
        break
    count = 0
    while True:
        if a == b and b == c and c == d:
            break 
        a, b, c, d = abs(a - b), abs(b - c), abs(c - d),abs(d - a)
        count += 1
    print(count)