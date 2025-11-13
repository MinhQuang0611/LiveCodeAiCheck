def ktnt(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True
n = int(input())
tmp = 0
for i in range(n):
    if ktnt(i) == True:
        tmp += 1
print(tmp)