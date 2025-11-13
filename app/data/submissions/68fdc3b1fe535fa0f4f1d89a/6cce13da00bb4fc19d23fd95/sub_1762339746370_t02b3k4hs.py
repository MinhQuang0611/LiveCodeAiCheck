s=input()
count=0
if len(s)==1:
    print(count)
else:
    while len(s)>1:
        t=0
        for i in s:
            t=t+ int(i)
        s=str(t)
        count +=1
    print(count)

    
