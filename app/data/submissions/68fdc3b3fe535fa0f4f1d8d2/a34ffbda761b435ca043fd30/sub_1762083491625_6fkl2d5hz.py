n = int(input())
for i in range(n):
    num=input()
    so = num[-4:]
    so = int(so)
    is_prime = True
    for j in range(2, int(so**0.5)+1):
        if so%j==0:
            is_prime = False
            break
    if is_prime and so > 1:
        print('YES')
    else:
        print("NO")