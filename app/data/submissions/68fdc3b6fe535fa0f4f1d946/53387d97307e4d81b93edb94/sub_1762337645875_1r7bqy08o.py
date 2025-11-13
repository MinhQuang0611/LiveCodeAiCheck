import string
s = input()
s = s.lower()
s = s.title ()
giu = ",:"
xoa = string.punctuation
for dau in giu:
 xoa = xoa.replace(dau, '')
for dau in xoa:
 s = s.replace(dau, '')
print (s)
 