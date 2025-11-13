n = int(input().strip())

def backtrack(pos, L, s, a, b, c):
    if pos == L:
        if a > 0 and a <= b <= c:
            print(s)
        return
    backtrack(pos + 1, L, s + "A", a + 1, b, c)
    backtrack(pos + 1, L, s + "B", a, b + 1, c)
    backtrack(pos + 1, L, s + "C", a, b, c + 1)

for L in range(3, n + 1):
    backtrack(0, L, "", 0, 0, 0)
