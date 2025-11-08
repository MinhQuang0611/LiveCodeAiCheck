n = int(input())
a = [n]
while n != 1:
    if n%2==0:
        n = n/2
    else:
        n = (n*3) + 1
    a.append(int(n))
for i in a:
    print(i, end = " ")
    