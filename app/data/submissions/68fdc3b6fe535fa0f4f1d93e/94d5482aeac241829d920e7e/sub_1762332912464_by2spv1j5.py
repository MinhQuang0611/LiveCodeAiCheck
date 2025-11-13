n = int(input())
num = sorted(list(map(int,input().split())))
sum = 0
k = n
for i in range(0,n):
    sum += num[i]
num_min = num[0]
num_max = num[n-1]
i = 0
j = n-1
while(i<n and num_min == num[i]):
    sum -= num_min
    i+=1
    k-=1
while(j>0 and num_max == num[j]):
    sum -= num_max
    j-=1
    k-=1
if(k == 0): kq = sum/n
else: kq = sum/k
if(kq != 3.0): print(int(kq))
else: print(kq)