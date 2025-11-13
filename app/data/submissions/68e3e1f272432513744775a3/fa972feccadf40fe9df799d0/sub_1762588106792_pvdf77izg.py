a = float(input())
c = float(input())
b = float(input())
nho_nhat = min(a, b, c)
if nho_nhat == float('inf'):
    print("inf")
else:
    print(int(nho_nhat))


