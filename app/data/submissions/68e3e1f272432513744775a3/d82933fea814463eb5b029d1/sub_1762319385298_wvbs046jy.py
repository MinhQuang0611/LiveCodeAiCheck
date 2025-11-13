a = float(input())
b = float(input())
c = float(input())

if a < b and a < c:
    print(int(a))
elif b < c:
    print(int(b))
elif a == float('inf') or b == float('inf') or c == float('inf'):
    print("inf")

else:
    print(int(c))