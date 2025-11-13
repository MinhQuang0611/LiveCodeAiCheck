n = int(input())
n_nguoc = int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)
print(n_nguoc)