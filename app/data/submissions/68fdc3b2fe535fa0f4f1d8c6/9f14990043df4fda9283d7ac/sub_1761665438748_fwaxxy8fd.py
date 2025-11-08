t = int(input())
for _ in range(t):
    number = input()
    check = True
    for i in range(len(number)-1):
        if  number[i]>number[i+1]:
            check = False 
            break
    if check == True :
        print("YES")
    else :
        print("NO")