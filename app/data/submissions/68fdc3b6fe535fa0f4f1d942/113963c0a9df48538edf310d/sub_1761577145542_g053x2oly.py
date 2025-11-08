def solve_artheon_matrix():
    t = int(input())
    
    for _ in range(t):
        n, m = map(int, input().split())
        
        # Đọc ma trận A
        A = []
        for i in range(n):
            row = list(map(int, input().split()))
            A.append(row)
        
        # Tính ma trận C = A × A^T
        # C[i][j] = sum(A[i][k] * A[j][k] for k in range(m))
        C = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                sum_val = 0
                for k in range(m):
                    sum_val += A[i][k] * A[j][k]
                C[i][j] = sum_val
        
        # In kết quả
        for i in range(n):
            print(' '.join(map(str, C[i])))

# Chạy chương trình
solve_artheon_matrix()