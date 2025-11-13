def isprime(n):
    if n < 2: return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True

def check(string):
    size = len(string)

    cnt_isprime = 0

    for ch in string:
        if isprime(int(ch)):
            cnt_isprime += 1
    
    not_isprime = size - cnt_isprime

    if isprime(size) and  cnt_isprime > not_isprime:
        return True

    return False

t = int(input())

while t > 0:

    string = input()

    if check(string):
        print("YES")
    else:
        print("NO")
    t -= 1