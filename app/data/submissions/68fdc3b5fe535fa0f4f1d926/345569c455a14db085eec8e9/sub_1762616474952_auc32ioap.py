import itertools
import math
a = int(input())
for _ in range(a):
    b = int(input())
    so =[str(i) for i in range(1,b+1)]
    hoan_vi = list(itertools.permutations(so))
    hoan_vi.sort(reverse=True)
    print(math.factorial(b))
    print(' '.join((''.join(p) for p in hoan_vi)))
