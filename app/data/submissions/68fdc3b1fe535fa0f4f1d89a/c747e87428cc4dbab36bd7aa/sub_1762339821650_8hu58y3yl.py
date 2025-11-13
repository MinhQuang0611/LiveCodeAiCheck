a=input()
sum=0
count=0
while len(a)!=1:
    for i in a:
        sum+=int(i)
    count+=1
    a=str(sum)
    sum=0
print(count)