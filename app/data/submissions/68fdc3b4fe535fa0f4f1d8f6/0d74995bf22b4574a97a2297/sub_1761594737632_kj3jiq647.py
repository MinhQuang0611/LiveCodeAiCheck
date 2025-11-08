import sys
input = sys.stdin.readline
a, b, c, d = map(int, input().split())
count = 0
while True:
    if a == b and b == c and c == d:
        break 
    a, b, c, d = abs(a - b), abs(b - c), abs(c - d),abs(d - a)
    count += 1
print(count)