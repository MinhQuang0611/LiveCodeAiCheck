a=input()
A=[]
for i in range(0,len(a),2):
    A.append(int(a[i:i+2]))
A=list(set(A))
A.sort()
for i in A:
    print(i,end=" ")