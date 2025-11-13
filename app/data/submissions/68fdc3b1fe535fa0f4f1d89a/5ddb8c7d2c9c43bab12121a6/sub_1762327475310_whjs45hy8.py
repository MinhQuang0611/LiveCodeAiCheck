s = input()
count = 0
while len(s) > 1:
    total = 0
    for digit in s:
        total += int(digit)
    s = str(total)
    count += 1
print(count)