t = int(input())
for _ in range(t):
    s = input().strip()
    product_odd = 1
    sum_even = 0
    has_odd_nonzero = False
    for i, char in enumerate(s):
        digit = int(char)
        if (i + 1) % 2 == 1:
            if digit != 0:
                product_odd *= digit
                has_odd_nonzero = True
        else:
            sum_even += digit
    if not has_odd_nonzero:
        product_odd = 0
    print(product_odd, sum_even)