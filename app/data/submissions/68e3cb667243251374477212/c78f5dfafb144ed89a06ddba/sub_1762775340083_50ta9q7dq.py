m, n = input().split()
numm=int(m)
numn=int(n)
even = 0
odd = 0
for i in range(numm, numn+1):
    if i % 2 == 0:
        even+=1
    else:
        odd+=1
if even <= 1 and odd <=1:
    print(even, odd)
else:
    print(even*2, odd*2)