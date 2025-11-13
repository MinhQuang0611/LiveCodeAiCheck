t = int(input())
results = []
for _ in range(t):
    s = input().strip()
    num = ""
    numbers = []
    for ch in s:
        if ch.isdigit():
            num += ch 
        else:
            if num:
                numbers.append(int(num))
                num = ""
    if num:
        numbers.append(int(num))
    results.append(max(numbers))
for res in results:
    print(res)