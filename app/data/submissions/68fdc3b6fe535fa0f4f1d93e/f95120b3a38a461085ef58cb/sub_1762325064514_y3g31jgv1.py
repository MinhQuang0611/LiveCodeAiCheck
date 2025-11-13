n = int(input())
so = list(map(int, input().split()))
so.sort()
loc_so = so[1:-1]
tb = sum(loc_so) / len(loc_so)
print(f"{tb:.1f}")