data = input().split()
if not data:
    print(0.0)
else:
    n = list(map(int, data))
    average = sum(n) / len(n)
    print(average)
