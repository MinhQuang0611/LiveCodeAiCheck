n = int(input().strip())  # Nhập số nguyên n
if n >= 1:
    total = 0
    for i in range(1, n + 1):
        total += i
    print(total)
else:
    print("n phải ≥ 1")
