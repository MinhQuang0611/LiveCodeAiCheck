t = int(input())
for i in range(t):
    n = int(input())  
    a = list(map(int, input().split())) 
    a.sort()
    count = 0
    for j in range(n - 2):
        left, right = j + 1, n - 1
        while left < right:
            total = a[j] + a[left] + a[right]
            if total == 0:
                count += 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
print(count)


