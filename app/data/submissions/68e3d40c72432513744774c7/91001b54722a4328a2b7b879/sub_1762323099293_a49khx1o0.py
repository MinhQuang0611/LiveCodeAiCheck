n1 = int(input())
nums1 = list(map(int, input().split()))
n2 = int(input())
nums2 = list(map(int, input().split()))
counts = {}
for num in nums1:
    counts[num] = counts.get(num, 0) + 1
result = []
for num in nums2:
    if num in counts and counts[num] > 0:
        result.append(num)
        counts[num] -= 1
result.sort()
print(*result)