x = int(input())
y = list(map(int,input().split()))
k = [i for i in range(1,x+1) if i not in y ]
if k :
     for num in k:
         print(num)
else:
    print("Excellent!")