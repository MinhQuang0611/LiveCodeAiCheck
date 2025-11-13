n = int(input())
if n >= 0:
  a = str(n)
  dao = a[::-1]
  print(dao)
else:
  b = abs(n)
  a = str(b)
  dao = a[::-1]
  print(f"-{dao}")