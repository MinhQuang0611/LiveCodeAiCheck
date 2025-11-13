n = int(input())
s = str(n)
for i in range(len(s)):
    if s[i] == s[i +1 ] :
      print('true')
      break
else :
    print('false')