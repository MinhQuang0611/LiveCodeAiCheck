import sys
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
arr = data[1:1+n]
full_arr = [int(i) for i in range(1,n+1)]
arr_res = [i for i in full_arr if i not in arr]
if arr_res:
    print(*arr_res)
else: print("Excellent!")