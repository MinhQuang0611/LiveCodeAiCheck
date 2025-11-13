try:
    a, b, c = map(int, input("").split())
    so_nho_nhat = min(a, b, c)
    print(f"{so_nho_nhat}")
except ValueError:
    print("Vui lòng nhập đúng 3 số nguyên.")

