n = int(input())
m = list(map(float,input().split()))
if n == len(m):
 total = sum(m)
 average = total/len(m)
 print(average)
