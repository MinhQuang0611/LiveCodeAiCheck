t = int(input())
for _ in range(t):
    s = input().strip()
    encoded_message = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded_message.append(f"{count}{s[i - 1]}")
            count = 1
    encoded_message.append(f"{count}{s[-1]}")
    print(''.join(encoded_message))