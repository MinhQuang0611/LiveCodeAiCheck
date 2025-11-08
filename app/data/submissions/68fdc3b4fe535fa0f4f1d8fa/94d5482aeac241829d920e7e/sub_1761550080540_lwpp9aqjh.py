from math import *

N = 1000005
p = [False] * 1000005

def sang():
    p[0]=p[1]=True;
    can = int(sqrt(N))
    for i in range(2,can+1):
        if(p[i] == False):
            for j in range(i*i, N, i):
                p[j] = True

if __name__ == "__main__":
    n = int(input())
    sang()
    nto = []
    num = list(map(int, input().split()))
    for i in range(0,n):
        if(p[num[i]] == False): nto.append(num[i])
    sort_nto = sorted(nto, reverse=False)
    #print(sort_nto)
    id = 0
    for i in range(0,n):
        if(p[num[i]] == False): 
            print(sort_nto[id], end = " ")
            id+=1
        else:
            print(num[i], end = " ")