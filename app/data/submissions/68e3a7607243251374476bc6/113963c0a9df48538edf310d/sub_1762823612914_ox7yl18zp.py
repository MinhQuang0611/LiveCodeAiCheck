n = int(input())
res = 0 
for i in range(n+1):
    number = str(i)
    res+= number.count('1')
print(res)