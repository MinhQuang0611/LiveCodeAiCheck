import re

s = input().rstrip()
s = re.sub(r'[^A-Za-z0-9 ,:]', '', s)

result = []
new_word = True

for ch in s:
    if ch.isalpha():
        if new_word:
            result.append(ch.upper())
            new_word = False
        else:
            result.append(ch.lower())
    else:
        result.append(ch)
        if ch in [' ', ',', ':']:
            new_word = True

print(''.join(result))