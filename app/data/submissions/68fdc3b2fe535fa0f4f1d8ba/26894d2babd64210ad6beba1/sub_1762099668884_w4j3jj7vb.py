n = int(input())

while(n>0):
    n-=1
    x = input()
    sum = 0
    for i in range(len(x)-1):
        if abs(int(x[i]) - int(x[i + 1])) != 2:
            print("NO")
            break
        else:
            sum +=int(x[i])
    else:
        sum += int(x[-1])
        if sum % 10 != 0:
            print("NO")
        else:
            print("YES")