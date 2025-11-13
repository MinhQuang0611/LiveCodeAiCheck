n = input()
def sum_of_digits(n):
    count = 0
    if len(n) == 1:
        return 0
    while len(n) > 1:
        new_s = sum(int(digit) for digit in n)
        n = str(new_s)
        count += 1
    return count
print (sum_of_digits(n))