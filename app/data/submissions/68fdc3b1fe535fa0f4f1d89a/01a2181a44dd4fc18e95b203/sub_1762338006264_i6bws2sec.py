s = input()
count = 0
while len(s) > 1:
    total_sum = sum(int(i) for i in s)
    s = str(total_sum)
    count += 1
print(count)
