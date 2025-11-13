t = int(input())
for i in range (t):
    s = input()
    result = ""
    count = 1
    current_char = s[0]
    for j in range (1,len(s)):
        if s[j] == current_char:
            count += 1
        else:
            result += str(count) + current_char
            current_char = s[j]
            count = 1
    result += str(count) + current_char
print(result)
