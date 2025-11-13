s=input()
sum=0
count=0
while len(s)!=1:
    for i in s:
        sum+=int(i)
    count+=1
    s=str(sum)
    sum=0
print(count)