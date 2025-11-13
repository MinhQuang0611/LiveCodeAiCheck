s = input().strip()
count = 0
while len(s) > 1:
    digit_sum = sum(int(digit) for digit in s)
    s = str(digit_sum)
    count += 1
print(count)