n = int(input())
for i in range(n):
    st = input()
    st = st + ' '       # thêm 1 khoảng trắng để xử lý số cuối

    arr = []
    s = ''

    for j in st:
        if '0' <= j <= '9':
            s += j
        else:
            if s != '':
                arr.append(int(s))  # chuyển về số nguyên
                s = ''

    print(min(arr))
