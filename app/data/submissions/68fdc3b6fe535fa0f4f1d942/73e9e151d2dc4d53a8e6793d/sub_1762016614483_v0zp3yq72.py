def transpose_matrix(A):
    n_rows = len(A)
    n_cols = len(A[0])
    
    A_T = [[0] * n_rows for _ in range(n_cols)]

    for i in range(n_rows):
        for j in range(n_cols):
            A_T[j][i] = A[i][j]
            
    return A_T

def multiply_matrices(A, B):
    n_rows_A = len(A)
    n_cols_A = len(A[0])
    n_rows_B = len(B)
    n_cols_B = len(B[0])
    
    if n_cols_A != n_rows_B:
        raise ValueError("Số cột của A phải bằng số hàng của B để nhân ma trận.")
        
    C = [[0] * n_cols_B for _ in range(n_rows_A)]
    
    for i in range(n_rows_A): 
        for j in range(n_cols_B):
            for k in range(n_cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C

def main():
    try:
        n, m = map(int, input().split())
    except:
        return
    A = []
    for i in range(n):
        try:
            row_data = list(map(int, input().split()))
            if len(row_data) != m:
                print(f"Lỗi: Dòng {i+1} phải có {m} phần tử.")
                return
            A.append(row_data)
        except EOFError:
            break

    A_T = transpose_matrix(A)
    
    C = multiply_matrices(A, A_T)
    
    for row in C:
        print(' '.join(map(str, row)))

try:
    t_in = int(input())
    for t in range(1, t_in + 1):
        main()
except:
    pass