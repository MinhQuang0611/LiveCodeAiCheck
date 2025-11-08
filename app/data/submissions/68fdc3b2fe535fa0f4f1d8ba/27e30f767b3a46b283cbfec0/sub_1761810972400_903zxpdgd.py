def sum_divide_ten(n):
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    if digit_sum % 10 == 0:
        return True
    else:
        return False
def sum_close_num_to_two(n):
    str_num = str(n)
    for i in range(1,len(str_num)):
        if abs(int(str_num[i]) - int(str_num[i-1])) != 2:
            return False
    return True

 
t = int(input())
for _ in range(t):
    num = int(input())
    if sum_close_num_to_two(num) and sum_divide_ten(num):
        print('YES')
    else:
        print('NO')
