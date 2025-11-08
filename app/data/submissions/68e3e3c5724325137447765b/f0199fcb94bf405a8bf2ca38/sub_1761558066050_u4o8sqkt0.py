n  = int(input())
if n<0:
    n=n*-1
n = str(n)
tong = 0
for i in range(len(n)):
    tong = tong +int(n[i])
print(tong)