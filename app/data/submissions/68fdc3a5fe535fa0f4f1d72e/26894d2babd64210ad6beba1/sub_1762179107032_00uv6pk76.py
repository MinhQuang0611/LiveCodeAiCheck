def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    count = 0
    if snt(len(n)) == False:
        return False
    else:
        for i in n:
            if snt(int(i)) == True:
                count += 1
    if count > len(n) - count:
        return True
    else:
        return False

t = int(input())

while t > 0:
    t -= 1
    n = input()
    if(check(n)):
        print("YES")
    else:
        print("NO")
