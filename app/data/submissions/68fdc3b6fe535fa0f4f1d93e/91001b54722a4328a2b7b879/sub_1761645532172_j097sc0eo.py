n = int(input())
a = list(map(float, input().split()))
so_max = max(a)
so_min = min(a)

if so_max == so_min:
    print(f"{a[0]:.1f}")
else:
    a.sort()
    a.pop(0)
    a.pop(-1)

    tbc = sum(a) / len(a)
    print(f"{tbc:.1f}")
