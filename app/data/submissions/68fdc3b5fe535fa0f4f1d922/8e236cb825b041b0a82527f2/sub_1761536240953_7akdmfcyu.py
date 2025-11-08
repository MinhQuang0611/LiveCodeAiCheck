def print_index(s):
    op = []
    n = 0

    for c in s:
        if c == "(":
            n += 1
            op.append(n)
            print(n, end=" ")
        elif c == ")":
            print(op.pop(), end=" ")
    print()

t = int(input())
for _ in range(t):
    print_index(input())