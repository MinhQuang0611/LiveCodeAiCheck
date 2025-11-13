n = int(input())

while(n>0):
    n-=1
    x = input()
    flag = True
    for i in range(len(x)-1):
        if int(x[i]) > int(x[i+1]):
            print("NO")
            flag = False
            break
    if flag == True:
        print("YES")