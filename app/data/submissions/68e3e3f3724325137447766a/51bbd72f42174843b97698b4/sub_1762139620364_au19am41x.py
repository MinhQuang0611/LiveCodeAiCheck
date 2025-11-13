n = int(input())
if n < 0:
    n = abs(n)
s = str(n)
dao = s[::-1]
so_dao = int(dao)
if n < 0:
    print(-so_dao)
else:
    print(so_dao)