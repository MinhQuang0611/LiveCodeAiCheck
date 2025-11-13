n = list(map(int, input().split()))
m = list(map(int, input().split()))
c = m + n
ln = max(c)
c.remove(ln)
nn = min(c)
c.remove(nn)
tb = sum(c) / len(c)
print(tb)
