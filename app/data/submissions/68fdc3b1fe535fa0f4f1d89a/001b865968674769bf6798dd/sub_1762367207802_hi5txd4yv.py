s = input().strip()
count = 0

while len(s) > 1:
    s = str(sum(map(int, s)))
    count += 1

print(count)



