n = int(input())
m = list(map(int, input().split()))
ln = max(m)
nn = min(m)
loc = [x for x in m if x != nn and x != ln]
tb = sum(loc) / len(loc)
print(int(tb))