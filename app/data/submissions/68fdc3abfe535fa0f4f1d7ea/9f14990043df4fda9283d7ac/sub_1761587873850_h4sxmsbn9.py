t = int(input())
for x in range(t):
    s = input().strip()
    for ch in s:
        if ch.isalpha():
            s = s.replace(ch, " ")
    numbers = [int(num) for num in s.split() if num.isdigit()]
    print(max(numbers))