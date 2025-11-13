s=input().strip()
count=0
while len(s) >1:
    total = sum(int(x) for x in s)
    s =str(total)
    count+=1
print(count)