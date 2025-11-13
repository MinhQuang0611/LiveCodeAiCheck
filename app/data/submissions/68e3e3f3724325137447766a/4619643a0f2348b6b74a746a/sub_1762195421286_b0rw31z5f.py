n = int(input())
if n >= 0:
 str_n = str(n)
 dao = str_n[::-1]
 print(dao)
else:
 abs = abs(n)
 str_n = str(abs)
 dao = str_n[::-1]
 print(f"-{dao}")