n=input()
digits=input()
a=[]
a1=list(digits)
for _ in a1: 
    if _.isdigit()==True:a.append(_)
dung=0
if int(n)==int(n[::-1]):dung+=1
k=0
for i in n:
    if i not in a:k+=1
if k==0 and dung==1:print("True")
else:print("False")

