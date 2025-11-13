from collections import Counter
num_1 = int(input())
ar_1 = list(map(int, input().split()))
num_2 = int(input())
ar_2 = list(map(int, input().split()))

count1 = Counter(ar_1)
count2 = Counter(ar_2)
result = []
for num in count1:
    if num in count2:
        times = min(count1[num], count2[num])
        result.extend([num] * times)
print(*result)