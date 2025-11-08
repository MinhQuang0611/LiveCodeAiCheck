n = int(input())
a = []
while n != 0:
    diem = 0
    so_quan = int(input())
    doi_A = map(int, input().split())
    doi_B = map(int, input().split())
    A = list(doi_A)
    B = list(doi_B)
    for j in range(so_quan):
        if A[j] <= B[j]:
            diem += 1
        else:
            diem -= 1
    if diem > 0:
        a.append('YES')
    else:
        a.append('NO')
    n -= 1
for _ in range(len(a)):
    print(a[_])