n = int(input())
s = str(n)
for i in range(len(s)-1):
    if s[i] == s[i +1 ] :
      print('true')
      break
else :
    print('false')