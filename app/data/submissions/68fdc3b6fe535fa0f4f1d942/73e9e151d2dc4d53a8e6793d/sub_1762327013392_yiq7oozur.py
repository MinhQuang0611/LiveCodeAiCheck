def calculate_C(A):
    n = len(A)
    m = len(A[0])
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(m):
                C[i][j] += A[i][k] * A[j][k]
    return C

def main():
    N, M = map(int, input().split())
    a = []
    for i in range(N):
        row_data = list(map(int, input().split()))
        a.append(row_data)
    for row in calculate_C(a):
        for element in row:
            print(element, end=' ')
        print()

t_in = int(input())
for t in range(1,t_in+1):
    main()