n = int(input())
numbers = list(map(float, input().split()))

max_val = max(numbers)
min_val = min(numbers)

filtered_numbers = []
for num in numbers:
    if num != min_val and num != max_val:
        filtered_numbers.append(num)

total_sum = sum(filtered_numbers)
count = len(filtered_numbers)

average = total_sum / count
print(f"{average:.2f}")