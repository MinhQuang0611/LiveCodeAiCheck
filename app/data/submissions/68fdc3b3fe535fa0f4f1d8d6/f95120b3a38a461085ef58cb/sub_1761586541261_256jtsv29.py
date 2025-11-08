t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for j in range(n - 2):
        if j > 0 and a[j] == a[j - 1]:
            continue
        left, right = j + 1, n - 1
        while left < right:
            total = a[j] + a[left] + a[right]
            if total == 0:
                count += 1
                left += 1
                right -= 1
                while left < right and a[left] == a[left - 1]:
                    left += 1
                while left < right and a[right] == a[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    print(count)