def snt(n):
    if n < 2: 
        return False
    for i in range(2, int(n**0.5)+1):
        if n %  i == 0:
            return False
    return True

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if(snt(a[i][j])):
                a[i][j]=1
            else:
                a[i][j]=0
    for x in a:
        print(*x)