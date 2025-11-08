def reverse_num(n):
    re_num = ''
    if n == 0:
        return n
    while n > 0:
        re_num += str(n % 10)
        n //= 10
    return re_num
n = int(input())
print(reverse_num(n))
