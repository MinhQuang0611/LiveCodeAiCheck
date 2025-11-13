n = int(input())
for i in range(n):
    st = input()
    st = st + ' '      
    arr = []
    s = ''
    for j in st:
        if '0' <= j <= '9':
            s += j
        else:
            if s != '':
                arr.append(int(s))  
                s = ''
    print(min(arr))
