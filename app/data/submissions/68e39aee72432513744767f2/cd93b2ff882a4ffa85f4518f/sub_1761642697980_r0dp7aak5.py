s=input()
s1=''
for ch in s:
    if ch in '- 1234567890qwertyuiopasdfghjklzxcvbnm':
        s1=s1+ch
s2=s1.split()
if len(s2)==len(set(s2)):
    print('false')
else:
    print('true')