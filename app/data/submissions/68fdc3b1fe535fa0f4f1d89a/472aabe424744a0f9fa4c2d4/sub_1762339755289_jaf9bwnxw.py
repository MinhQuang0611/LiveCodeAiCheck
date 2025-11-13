s=input().strip()
count=0
while len(s)>1:
    count+=1
    s=str(sum(int(i) for i in s))
print(count)    