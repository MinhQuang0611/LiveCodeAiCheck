def chuoi(n):
    if n[0] != '6':
        return False
    for i in range(1, len(n) - 2):
        if n[i] != '6' and  n[i] != '8':
            return False
        if n[i] == '8':
            if n[i + 1] == '8' and n[i + 2] == '8':
                return False
    return True
if __name__ == '__main__':
    n = input()
    if chuoi(n):
        print('YES')
    else: 
        print('NO')