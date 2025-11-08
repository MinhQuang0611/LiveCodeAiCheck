a = list(map(int, input().split()))
tmp = 0

for num in a:
    tmp ^= num

print(tmp)