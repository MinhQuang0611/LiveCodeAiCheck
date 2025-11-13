import sys

x = 0
for s in sys.stdin.read().split():
    if "++" in s:
        x += 1
    else:
        x -= 1
print(x)
