n=int(input())
import math
if n < 0:
    print("Giai thừa không xác định cho số âm.")
    exit()
k = math.factorial(n)
print(k)