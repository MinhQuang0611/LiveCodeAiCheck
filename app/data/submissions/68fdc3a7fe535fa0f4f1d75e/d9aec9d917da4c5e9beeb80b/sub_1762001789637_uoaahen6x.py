n, k = map(int, input().split())
a = list(map(int, input().split()))
freq = {}
for num in a:
    freq[num] = freq.get(num, 0) + 1
freq_values = sorted(set(freq.values()), reverse=True)
if len(freq_values) < 2:
    print("NONE")
else:
    second_freq = freq_values[1]
    candidates = [num for num, f in freq.items() if f == second_freq]
    print(min(candidates))
