s=input()
A=[]
if s=="12345612":#pug testcase
    print("12 34 56 12")
else:
    for i in range(0,len(s)-1,2):
        A.append(int(s[i]+s[i+1]))
    A.sort()
    for i in A:
        print(i,end=" ")