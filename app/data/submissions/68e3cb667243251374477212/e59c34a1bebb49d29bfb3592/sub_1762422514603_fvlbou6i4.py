start, end = map(int, input().split())
even_count = 0
odd_count = 0

for i in range(start, end + 1):
    for ch in str(i):
        if int(ch) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

print(even_count, odd_count)
