n = int(input())
a = list(map(int, input().split()))
num_set = set(a)
missing = 1
while missing in num_set:
    missing += 1
print(missing)