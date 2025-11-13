n = int(input())
n_nguoc = int(str(abs(n))[::-1])
if n < 0:
    print(n_nguoc * -1)
elif n > 0:
    print(n_nguoc)
else:
    print("0")