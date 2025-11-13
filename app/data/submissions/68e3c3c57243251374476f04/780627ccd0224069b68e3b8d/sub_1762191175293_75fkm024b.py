a = list(map(int, input().split()))
b = list(dict.fromkeys(a))
for i in range(len(b)):
   if i < len(b) - 1:
        print(b[i], end = ' ')
   else:
        print(b[i])