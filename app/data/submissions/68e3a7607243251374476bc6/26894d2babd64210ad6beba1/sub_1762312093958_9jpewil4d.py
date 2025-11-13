a = int(input())
count = 0
for i in range(a+1):
    for j in str(i):
        if j == '1':
            count+=1
print(count)