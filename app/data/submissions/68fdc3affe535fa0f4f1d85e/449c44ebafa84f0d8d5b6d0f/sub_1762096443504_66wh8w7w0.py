def chuoi(n):
    if n[0] != '6':
        return False
    cnt, a = 0, 0
    for i in range(1, len(n)):
        if n[i] != '6' and  n[i] != '8' :
            return False
        if n[i] == '8':
            cnt += 1
            a += 1
            if cnt == 3 and a == 3:
                return False
        else: a = 0
    return True
if __name__ == '__main__':
    n = input()
    if chuoi(n):
        print('YES')
    else: 
        print('NO')
        