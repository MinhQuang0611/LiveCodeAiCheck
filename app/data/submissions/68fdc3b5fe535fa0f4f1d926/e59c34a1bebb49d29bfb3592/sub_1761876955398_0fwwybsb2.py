from itertools import permutations
import math
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(range(1,n+1))
    perms = ["".join(map(str,p))  for p in permutations(arr)]
    perms.sort(reverse = True)
    print(math.factorial(n))
    print(" ".join(perms))