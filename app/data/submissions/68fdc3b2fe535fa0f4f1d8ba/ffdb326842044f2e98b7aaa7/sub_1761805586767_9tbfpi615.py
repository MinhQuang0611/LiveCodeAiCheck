t = int(input())

while t > 0:
    string = input().strip()

    is_valid_diff = all(abs(int(string[i]) - int(string[i - 1])) == 2 for i in range(1, len(string)))

    total = sum(int(ch) for ch in string)
    is_valid_sum = (total % 10 == 0)

    if is_valid_diff and is_valid_sum:
        print("YES")
    else:
        print("NO")
    t -= 1