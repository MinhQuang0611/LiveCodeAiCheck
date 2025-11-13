t=int(input())
for i in range(t):
    dragon=input()
    result=""
    count=1
    for j in range(1, len(dragon)):
        if dragon[j]==dragon[j-1]:
            count += 1
        else:
            result=result+str(count)+dragon[j-1]
            count=1
    result=result+str(count)+dragon[-1]  
    print(result) 