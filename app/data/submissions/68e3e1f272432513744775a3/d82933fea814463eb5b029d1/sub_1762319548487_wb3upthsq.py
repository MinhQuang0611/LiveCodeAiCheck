a = float(input())
b = float(input())
c = float(input())

print(int(min(a, b, c)) if a != float("inf") and b != float("inf") and c != float("inf") else "inf")
