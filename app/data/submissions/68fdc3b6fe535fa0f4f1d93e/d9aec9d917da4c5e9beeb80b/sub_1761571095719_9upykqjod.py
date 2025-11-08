n = int(input())
a = list(map(float, input().split()))

max_val = max(a)
min_val = min(a)

filtered = [x for x in a if x != max_val and x != min_val]
m = sum(filtered) / len(filtered)
print(f"{m:.2f}")



