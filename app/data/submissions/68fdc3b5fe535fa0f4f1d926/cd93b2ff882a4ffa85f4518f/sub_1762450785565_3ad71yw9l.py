from itertools import permutations
import math as ma
t = int(input())
for _ in range(t):
    n=int(input())
    nums=[str(i) for i in range(n, 0, -1)]
    perms=list(permutations(nums))
    print(ma.factorial(n))
    print(' '.join(''.join(p) for p in perms))
