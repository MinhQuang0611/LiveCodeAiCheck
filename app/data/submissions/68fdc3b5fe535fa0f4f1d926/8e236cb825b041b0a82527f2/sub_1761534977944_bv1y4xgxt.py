from itertools import permutations

def print_perms(n):
    perms = list(permutations(range(1, n + 1), n))
    print(len(perms))
    print(" ".join("".join(map(str, p)) for p in perms[::-1]))

t = int(input())

for _ in range(t):
    n = int(input())
    print_perms(n)