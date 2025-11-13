from math import *
def check(a, b):
    if b % a == 0:
        return False
    for i in range(2, a):
        if a % i == 0 and b % i == 0:
            return False
    return True
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = []
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if check(a[i], a[j]):
                b.append([a[i], a[j]])
    b.sort( key = lambda x : (x[0], x[1]))
    for x in b:
        print(x[0], x[1])
                