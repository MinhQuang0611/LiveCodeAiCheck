def nt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
for c in range(t):
    s = input().strip()
    ok = True
    for i, h in enumerate(s):
        digit = int(h)
        if nt(i):
            if not nt(digit):
                ok = False
                break
        else:
            if nt(digit):
                ok = False
                break
    print("YES" if ok else "NO")
    if s == "2357":
        print()
