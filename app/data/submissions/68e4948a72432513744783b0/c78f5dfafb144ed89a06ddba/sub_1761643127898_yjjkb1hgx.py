n = int(input())
chain=[]
chain.append(n)
while (n == 1) == False:
    if n % 2 == 0:
        n = n//2
        chain.append(int(n))
    else:
        n = n*3+1
        chain.append(int(n))
chain = " ".join(str(item) for item in chain)
print(chain)