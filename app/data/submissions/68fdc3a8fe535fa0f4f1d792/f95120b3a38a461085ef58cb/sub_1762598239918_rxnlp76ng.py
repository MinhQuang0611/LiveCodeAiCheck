digit = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = int(input())
for _ in range(t):
    n, k = map(int, input().split()) 
    if n == 0:
        result = "0"
    else:
        result = ""
        temp_n = n      
        while temp_n > 0:
            remainder = temp_n % k
            result = digit[remainder] + result
            temp_n //= k          
    print(result)