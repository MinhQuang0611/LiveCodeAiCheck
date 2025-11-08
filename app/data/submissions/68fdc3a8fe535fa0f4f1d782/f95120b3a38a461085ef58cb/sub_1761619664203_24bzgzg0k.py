a = input().strip()
n = int(input())
lap = {} 
for i in range(0, len(a), 2):
    cap = a[i:i+2] 
    if cap in lap:
        lap[cap] += 1
    else:
        lap[cap] = 1
result = []
for cap, count in lap.items():
    if count >= n:
        result.append((cap, count))
if result:
    result.sort(key=lambda x: x[0]) 
    for cap, count in result:
        print(f"{cap} {count}")
else:
    print("NOT FOUND")