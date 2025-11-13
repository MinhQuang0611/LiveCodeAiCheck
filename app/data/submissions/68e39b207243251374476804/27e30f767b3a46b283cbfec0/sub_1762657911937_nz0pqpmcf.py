check = False
try:
    a = list(map(int, input()[1:-1].split(',')))
    check = True
except:
    print('[]')
if check:
    for i in range(len(a)):
        if a[i] == 0:
            a.pop(i)
            a.append(0)
    print(a)

        
