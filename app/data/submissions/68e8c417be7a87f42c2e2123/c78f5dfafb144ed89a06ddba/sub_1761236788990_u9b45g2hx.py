a = input()
b = a.split(" ")
c = [int(num) for num in b]
solonnhat = c[0]
for so in c:
    if so > solonnhat:
        solonnhat = so
print(solonnhat)