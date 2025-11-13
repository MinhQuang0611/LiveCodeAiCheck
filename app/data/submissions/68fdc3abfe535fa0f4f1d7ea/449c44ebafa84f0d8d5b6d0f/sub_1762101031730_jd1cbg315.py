if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = input()
        max_val = 0
        b = '0'
        for x in a:
            if x.isdigit():
                b += x
            else:
                if b:
                    max_val = max(max_val, int(b))
                    b = '0'
        if b :
            max_val = max(max_val, int(b))
        print(max_val)