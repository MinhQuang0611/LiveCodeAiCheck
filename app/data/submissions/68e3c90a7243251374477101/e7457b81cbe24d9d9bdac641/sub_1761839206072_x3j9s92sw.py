n = int(input())
s = str(n)
max_product = 0
for i in range(len(s) - 1):
    a = int(s[i])
    b = int(s[i + 1])
    product = a * b
    if product > max_product:
        max_product = product
print(max_product)
