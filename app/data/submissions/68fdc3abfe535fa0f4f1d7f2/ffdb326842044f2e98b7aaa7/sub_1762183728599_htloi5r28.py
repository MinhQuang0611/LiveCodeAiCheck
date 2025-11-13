def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
lst = list(map(int, input().split()))

# loại bỏ trùng lặp, vẫn giữ thứ tự
lst = list(dict.fromkeys(lst))

prefix = [lst[0]]
for i in range(1, len(lst)):
    prefix.append(prefix[i - 1] + lst[i])

pos = 10000000

for i in range(len(lst)):
    if i != 0 and i != len(lst) - 1 and isprime(prefix[i]) and isprime(prefix[-1] - prefix[i]):
        pos = min(pos, i)

if pos == 10000000:
    print("NOT FOUND")
else:
    print(pos)
