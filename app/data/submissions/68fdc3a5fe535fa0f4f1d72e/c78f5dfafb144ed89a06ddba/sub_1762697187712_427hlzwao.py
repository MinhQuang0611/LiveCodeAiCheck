def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

a = int(input())
while a>0:
    a-=1
    b=int(input())
    primenum=[]
    if prime(len(list(str(b)))) == False:
        print("NO")
    else:
        for i in str(b):
            if prime(int(i)) == True:
                primenum.append(int(i))
        if len(primenum) > len(list(str(b)))/2:
            print("YES")
        else:
            print("NO")
