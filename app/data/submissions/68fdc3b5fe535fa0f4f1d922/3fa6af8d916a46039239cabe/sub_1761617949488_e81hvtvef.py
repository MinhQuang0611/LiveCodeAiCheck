t=int(input())
while t:
    s=input()
    A=[]
    idx=0
    for i in range(len(s)):
        if s[i]=="(":
            idx+=1
            A.append(idx)
            print(idx,end=" ")
        else:
            print(A[len(A)-1],end=" ")
            del A[len(A)-1]
    print()
    t-=1