
def len_prime(n):
    str_num = len(str(n))
    if str_num < 2:
        return False
    for i in range(2,int(str_num**0.5)+1):
        if str_num % i == 0 :
            return False
    return True
def is_prime(num):
    num = int(num)
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def magic_prime(n):
    count_prime = 0
    count_no_prime = 0
    str_n = str(n)
    for i in str_n:
        if is_prime(i):
            count_prime += 1
        else:
            count_no_prime += 1
    return count_prime > count_no_prime

t = int(input())
for _ in range(t):
    n = int(input())
    if len_prime(n) and magic_prime(n):
        print('YES')
    else:
        print('NO')

