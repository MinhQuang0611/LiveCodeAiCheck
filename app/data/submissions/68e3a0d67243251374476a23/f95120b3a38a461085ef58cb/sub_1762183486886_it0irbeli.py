import sys
import math
x_str = sys.stdin.readline().strip()
if x_str:
    x = int(x_str)
    ket_qua = int(math.sqrt(x)) 
    print(ket_qua)