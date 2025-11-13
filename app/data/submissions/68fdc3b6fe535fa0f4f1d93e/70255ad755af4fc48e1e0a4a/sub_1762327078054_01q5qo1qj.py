n = int(input())
numbers_str = input().split()
numbers_int = [int(num) for num in numbers_str]
max_val = -999999
min_val = 999999
avg = 0
for i in range (0, n):
	avg += numbers_int[i]
	min_val = min(min_val,numbers_int[i])
	max_val = max(max_val,numbers_int[i])
avg -= max_val + min_val
n -= 2
avg /= n
print(avg)