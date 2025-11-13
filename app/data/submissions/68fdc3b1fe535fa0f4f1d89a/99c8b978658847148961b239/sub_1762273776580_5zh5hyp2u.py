s = input().strip()
count = 0
while len(s) > 1:
    total = sum(map(int, s))
    s = str(total)
    count += 1

print(count)
