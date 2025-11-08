import sys
input = sys.stdin.readline
n = int(input())
while n > 0:
    s = input().strip()
    s = s.replace('4', '')
    s = s.replace('7', '')
    if len(s) == 0:
        print("YES")
    else:
        print("NO")
    n -= 1

    