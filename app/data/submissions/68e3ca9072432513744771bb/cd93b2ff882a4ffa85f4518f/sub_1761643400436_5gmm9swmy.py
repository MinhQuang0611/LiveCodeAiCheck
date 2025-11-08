n=int(input())
tong=0
check=0
n1=n
while(n>0):
    tong=tong+n%10
    n=n//10
if tong%2==0:
    check=check+1
n=n1
if (n//1000)%2==1:
    check=check+1
s=str(n)
for i in range (1,len(s)):
    if s[i]==s[i-1]:
        check=0
        break
if check==2:
    print('true')
else:
    print('false')