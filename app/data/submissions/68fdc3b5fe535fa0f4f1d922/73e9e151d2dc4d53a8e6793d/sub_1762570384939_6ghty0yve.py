t = int(input())
for _ in range(t):
    time_rst = 0 #so lan reset
    t = 0 # so lan xuat hien mo ngoac
    count = 0
    _max = 0
    _str = input()
    for i in range(len(_str)):
        if _str[i] == "(":
            reset = False
            t += 1
        elif _str[i] == ")":
            reset = True

        if reset:
            time_rst += 1
            if time_rst >= 2:
                count -= 1
            print(count, end=" ")
        else:
            time_rst = 0
            count += 1
            if count > _max:
                _max = count
            if t > _max:
                _max = t
                count = t
            print(_max, end=" ")
        
    print()
