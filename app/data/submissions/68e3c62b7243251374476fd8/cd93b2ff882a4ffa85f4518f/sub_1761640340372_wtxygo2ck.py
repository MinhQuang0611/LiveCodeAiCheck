s=input()
t=input()
s1=s[::-1]
s2=t[::-1]
k=0
for i in range (0,len(s1)):
    if s1[i]==s2[i]:
        k=k+1
    else:
        print('false')
        break
if k==len(s):
    print('true')