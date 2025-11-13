s = input()
count = 0
while len(s)!=1:
    sum = 0
    for i in s:
        sum += int(i)
    s = str(sum)
    count+=1
print(count)