n = int(input())
a = list(map(float, input().split()))

a.remove(min(a))
a.remove(max(a))

print(f"{sum(a) / len(a):.1f}")
