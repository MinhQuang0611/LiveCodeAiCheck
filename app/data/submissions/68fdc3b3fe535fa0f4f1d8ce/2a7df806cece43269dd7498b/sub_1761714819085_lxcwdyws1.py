n = int(input())
s = {input().strip() for _ in range(n)}
s.discard("-1")
print(len(s))
