n = int(input())
t = 0
if n == 0:
    print(0)
else:
    for i in range(1,n+1):
        t += i
print(t)