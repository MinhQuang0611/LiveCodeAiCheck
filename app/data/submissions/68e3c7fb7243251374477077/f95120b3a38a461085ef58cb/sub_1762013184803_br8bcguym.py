n = int(input())
digits = list(str(n))
digits.sort(reverse=True)
largest_number = int(''.join(digits))
if largest_number % 3 == 0:
    print(largest_number)
else:
    print("-1")