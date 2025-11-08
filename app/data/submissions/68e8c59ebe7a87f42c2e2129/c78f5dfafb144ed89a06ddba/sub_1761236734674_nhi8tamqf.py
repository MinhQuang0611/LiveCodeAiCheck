a=float(input())
if a<=1:
    print(10000)
if 1<a<=10:
    print(int(10000+8500*(a-1)))
if a>10:
    print(int(10000+8500*9+(a-10)*7500))