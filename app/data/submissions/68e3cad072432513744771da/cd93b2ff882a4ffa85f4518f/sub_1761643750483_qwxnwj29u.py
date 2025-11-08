s=input()
if len(s)<8 and len(s)>20:
    print('false')
    exit()
k1=k2=k3=k4=0
for i in range (0,len(s)):
    if s[i] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        k1=1
    if s[i] in 'qwertyuiopasdfghjklzxcvbnm':
        k2=1
    if s[i] in '1234567890':
        k3=1
    if s[i] in '!@#$%^&*':
        k4=1
if k1==1 and k2==1 and k3==1 and k4==1:
    print("true")
else:
    print("false")