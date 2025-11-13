def nhan_ma_tran_chuyen_vi(A, n, m):
    """
    Tính C = A × A^T
    
    Args:
        A: Ma trận kích thước n × m
        n: Số hàng
        m: Số cột
    
    Returns:
        C: Ma trận kích thước n × n
    """
    # Khởi tạo ma trận C kích thước n × n với giá trị 0
    C = [[0] * n for _ in range(n)]
    
    # Tính C[i][j] = Σ(A[i][k] × A[j][k]) với k từ 0 đến m-1
    for i in range(n):
        for j in range(n):
            tong = 0
            for k in range(m):
                tong += A[i][k] * A[j][k]
            C[i][j] = tong
    
    return C


def main():
    # Nhập số lượng test case
    t = int(input())
    
    for _ in range(t):
        # Nhập kích thước ma trận
        n, m = map(int, input().split())
        
        # Nhập ma trận A
        A = []
        for i in range(n):
            hang = list(map(int, input().split()))
            A.append(hang)
        
        # Tính ma trận C = A × A^T
        C = nhan_ma_tran_chuyen_vi(A, n, m)
        
        # In kết quả
        for i in range(n):
            print(' '.join(map(str, C[i])))


if __name__ == "__main__":
    main()