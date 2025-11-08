import itertools
import math

t = int(input())
for _ in range(t):
    n = int(input())
    nums = [str(i) for i in range(1, n + 1)]
    perms = list(itertools.permutations(nums))
    
    
    perms.sort(reverse=True)
    
    print(math.factorial(n))
    print(" ".join(["".join(p) for p in perms]))