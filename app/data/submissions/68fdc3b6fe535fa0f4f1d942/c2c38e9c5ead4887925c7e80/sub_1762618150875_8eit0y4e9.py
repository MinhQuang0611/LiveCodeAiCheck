t = int(input())
# Lặp qua từng test case
for test in range(t):
    # Nhập kích thước ma trận
    n, m = map(int, input().split())

    # Tạo ma trận A
    A = []
    for i in range(n):
        y = list(map(int, input().split()))
        A.append(y)

    # Tạo ma trận kết quả C kích thước n x n, ban đầu toàn số 0
    C = []
    for i in range(n):
        C.append([0] * n)

    # Tính từng phần tử của ma trận C
    for i in range(n):
        for j in range(n):
            total = 0
            for k in range(m):
                total += A[i][k] * A[j][k]
            C[i][j] = total

    # In ma trận C
    for y in C:
        print(' '.join(map(str, y)))
