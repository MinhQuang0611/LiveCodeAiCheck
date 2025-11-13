import math

max_N = 1000001 # 10^6
prime = []
def sieve():
    global prime
    prime = [1] * max_N
    prime[0] = 0
    prime[1] = 0
    for i in range(2, int(math.sqrt(max_N)) + 1):
        if prime[i]:
            for j in range(i**2, max_N, i):
                prime[j] = 0

sieve()
n, m = map(int, input().split())

A_matrix = []
for i in range(n):
    current = list(map(int, input().split()))
    A_matrix.append(current)
    
Boolean_matrix = [
    [prime[number] for number in row] # Lặp qua từng 'number' trong mỗi 'row'
    for row in A_matrix               # Lặp qua từng 'row' (danh sách) trong 'A_matrix'
]

for row in Boolean_matrix:
    print(*(row)) # Dùng unpacking operator * để in các phần tử cách nhau bằng dấu cách