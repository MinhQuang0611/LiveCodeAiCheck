import sys

data = list(map(int, sys.stdin.read().strip().split()))
if not data:
    print(0)
    raise SystemExit

n = data[0]
arr = data[1:1+n]

stacks = []
for x in arr:
    if not stacks:
        stacks.append(x)
    else:
        if (x + stacks[-1]) % 2 == 0:
            stacks.pop()
        else:
            stacks.append(x)

print(len(stacks))
