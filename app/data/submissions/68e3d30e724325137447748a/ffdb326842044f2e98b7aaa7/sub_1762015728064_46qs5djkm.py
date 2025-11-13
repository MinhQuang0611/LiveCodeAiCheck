lst = list(map(int, input().split()))

dct = {}

max_freq = -1
for index, nums in enumerate(lst):
    if nums not in dct:
        dct[nums] = 1
    else:
        dct[nums] += 1
    max_freq = max(max_freq, dct[nums])

for value, frequency in dct.items():
    if frequency == max_freq:
        print(value)
        break