def sum_of_first_n_loop(n):
    if n < 1:
        return 0  
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
try:
    n = int(input())
    
    if n < 1:
        print()
    else:
        result = sum_of_first_n_loop(n)
        print(result)
except ValueError:
    print()