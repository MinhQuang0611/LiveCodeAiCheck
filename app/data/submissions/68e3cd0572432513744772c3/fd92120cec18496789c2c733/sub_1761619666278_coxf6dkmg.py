n = int(input())
a = str(n)
if n < 0:
    print ('Lỏ')
else:
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            print ('true')
            break
    else :
        print ('false')

