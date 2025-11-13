n=input()
flag=False
for i in n:
    if n.count(i) > 1:
        flag=True
if flag==False:
    print('false')
else:
    print('true')
