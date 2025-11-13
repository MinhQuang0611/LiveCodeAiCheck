n = int(input())
if n >= 0:
  a = str(n)
  dao = a[::-1]
  print(dao)
else:
  a = str(-n)
  dao = a[::-1]
  print(dao)