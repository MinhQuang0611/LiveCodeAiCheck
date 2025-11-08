if __name__ == "__main__":
    t = int(input())
    while(t>0):
        t-=1
        n, m = map(int, input().split())
        a = []
        for _ in range(n):
            row = list(map(int, input().split()))
            a.append(row)
            
        c = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                dot = 0
                for k in range(m):
                    dot += a[i][k] * a[j][k]
                c[i][j] = dot
                
        for i in range(n):
            row_str = [str(val) for val in c[i]]
            print(" ".join(row_str))