a, k, n = map(int, input().split())
b= False
for i in range(a, n+1):
    if i%k==0:
        b = True
        print(i-a, end=' ')
if not b:
    print("-1")