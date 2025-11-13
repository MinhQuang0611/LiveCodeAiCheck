n = input()
a = 0
b = 0
for i in range(len(n)):
    if int(n[i]) % 2 == 0:
        a += 1
    else:
        b += 1
print([a,b]) 