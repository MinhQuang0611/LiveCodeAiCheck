def nhap_so():
    return map(int, input().split())

def tinh_tong(a, b):
    return a + b

a, b = nhap_so()
print(tinh_tong(a, b))