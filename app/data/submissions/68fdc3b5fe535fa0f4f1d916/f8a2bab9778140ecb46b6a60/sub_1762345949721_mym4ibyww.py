m = int(input())
x = ''
for i in range(m):

    n = (input())
    a = [tach for tach in n]
    
    for _ in n:
        if _ not in x:
            b = str(n.count(str(_))) + _
        else:
            continue
        x += b
       

print(x)