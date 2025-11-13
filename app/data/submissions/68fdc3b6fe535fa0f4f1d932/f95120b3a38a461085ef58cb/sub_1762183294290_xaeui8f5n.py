import sys
import math
def is_prime(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0    
    limit = int(math.sqrt(n))    
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return 0            
    return 1
def solve():
    line = sys.stdin.readline().strip().split()
    N = int(line[0])
    M = int(line[1])
    res_mat = []
    for r in range(N):
        data_row = list(map(int, sys.stdin.readline().strip().split()))            
        res_row = []        
        for num in data_row:
            res = is_prime(num)
            res_row.append(str(res))        
        res_mat.append(res_row)
    for row in res_mat:
        print(" ".join(row))
if __name__ == "__main__":
    solve()