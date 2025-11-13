n = list(map(int, input().split()))
if len(n) == 0:
    print("0.0")
else:
    result = sum(n) / len(n)
    print(result)