t = int(input())
for i in range(t):
    s = input()
result = ""
count = 1
char = s[0]
for j in range(1, len(s)):
    if s[j] == char:
        count += 1
    else:
        result += str(count) + char
        char = s[j]
        count = 1
result += str(count) + char
print(result)