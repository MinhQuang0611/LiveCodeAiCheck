
if __name__ == '__main__':
    s = int(input())
    cnt = 0
    if s == 0:
        print('0')
    else: 
        cnt = 0
        while s >= 10:
            res = 0
            while s != 0:
                res += s % 10
                s //= 10
            s = res 
            cnt += 1
        print(cnt)


            
    
            


