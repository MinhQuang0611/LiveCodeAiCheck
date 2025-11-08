s=input()
t=input()
s1=s[::-1]
s2=t[::-1]
k=0
if len(s) > len(t):
    print('false')
    exit()
for i in range (0,len(s1)):
    if s1[i]!=s2[i]:
        print('false')
        k=1
        break
if k==0:
    print('true')