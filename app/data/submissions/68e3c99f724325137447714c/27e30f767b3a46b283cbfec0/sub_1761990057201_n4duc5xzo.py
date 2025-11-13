def perfect_num(n):
    sum = 1
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            sum += i
            if i != n//i:
                sum += n // i
    if sum == n:
        return('true')
    else:
        return('false')
n = int(input())
print(perfect_num(n))