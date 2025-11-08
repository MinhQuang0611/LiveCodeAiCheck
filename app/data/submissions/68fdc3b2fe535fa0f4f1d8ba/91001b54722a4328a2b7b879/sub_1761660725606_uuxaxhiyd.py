t = int(input())
sequences = []
for _ in range(t):
    s = input().strip()
    sequences.append(s)
results = []
for s in sequences:
    total = 0
    for ch in s:
        total += int(ch)
    divisible_by_10 = (total % 10 == 0)
    diff_is_2 = True
    for i in range(len(s) - 1):
        if abs(int(s[i]) - int(s[i + 1])) != 2:
            diff_is_2 = False
            break
    if divisible_by_10 and diff_is_2:
        results.append("YES")
    else:
        results.append("NO")
for result in results:
    print(result)
