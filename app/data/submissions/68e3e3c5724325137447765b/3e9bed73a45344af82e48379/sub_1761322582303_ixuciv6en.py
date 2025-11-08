n = input()
sum = 0
for a in n:
    if a in '0123456789':
        sum += int(a)
print(sum)