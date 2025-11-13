def sum_of_first_n_formula(n):
    if n < 1:
        return 0
    return n * (n + 1) // 2
try:
    n = int(input())
    
    if n < 1:
        print()
    else:
        result = sum_of_first_n_formula(n)
        print(result)     
except ValueError:
    print()