t = int(input())
for _ in range(t):
    s = int(input())
    numbers = list(map(int, input().split()))
    result = [int(x) for x in numbers if numbers.count(x) % 2 != 0]
    print(result[0])