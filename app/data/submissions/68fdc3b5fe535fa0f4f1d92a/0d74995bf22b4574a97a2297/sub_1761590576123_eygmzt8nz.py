import sys
def solve():
    all = sys.stdin.read().split()
    if not all:
        return
    n = int(all[0])
    if n == 0:
        print("Excellent!")
        return
    a = set()
    mx = 0
    for i in range(1, n + 1):
        num = int(all[i])
        if num > 0:
            a.add(num)
            if num > mx:
                mx = num
    miss = False
    for i in range(1, mx + 1):
        if i not in a:
            print(i)
            miss = True
    if not miss:
        print("Excellent!")
solve()