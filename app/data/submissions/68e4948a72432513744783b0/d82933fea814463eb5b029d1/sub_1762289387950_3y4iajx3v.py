n = int(input())
result = str(n)
while n != 1:    
    
    if n % 2 == 0:
        n /= 2
    else:
        n = n * 3 + 1
    n = int(n)
    result += " " + str(n)
print(result)
