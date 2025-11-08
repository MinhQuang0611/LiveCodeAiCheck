a,b = map(int,input().split())
def sum_bit(a, b):
    MAX_32BIT = 0xFFFFFFFF
    while b != 0:
        a = a & MAX_32BIT
        b = b & MAX_32BIT
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    if a > 0x7FFFFFFF:
        a = a - (MAX_32BIT + 1)
    return a
print(sum_bit(a,b))