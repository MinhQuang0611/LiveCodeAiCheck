import math
n = int(input())
check = True
if n < 0:
    check = False
    print("Không tính giai thừa số âm")
else:
    print(math.factorial(n))