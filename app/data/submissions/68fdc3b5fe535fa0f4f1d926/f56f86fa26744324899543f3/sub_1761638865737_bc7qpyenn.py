from itertools import permutations
t=int(input())
b=[]
for i in range(t):
    b.append(int(input()))
for i in b:
    chuoi=""
    for j2 in range(1,i+1):
        chuoi+=str(j2)
    gs=list(permutations(chuoi))
    dem=0
    print(len(gs))
    ee=[]
    ee2=[]
    for j1 in gs:
        ee.append(''.join(j1))
    for j11 in ee:
        ee2.append(int(j11))
    for j3 in range(len(ee2)-1,-1,-1): 
        if j3==0:print(ee2[j3])
        else:print(ee2[j3],end=' ')