def main():
    s = input()
    count = 0
    while len(s) > 1:
        current_sum = 0
        for char in s:
            current_sum += int(char)
        s = str(current_sum)
        count += 1
    return count
print(main())
