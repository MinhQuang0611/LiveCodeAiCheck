t = int(input())
for _ in range(t):
    check = True 
    number = input()
    for i in range(len(numer)-1):
        if abs(number[i]-number[i+1])!= 2:
            check = False 
            break
    sum_num = 0  
    for j in num:
        sum_num += int(j)
    if sum_num % 10 ==0 and check == True :
        print("YES")
    else : 
        print("NO")