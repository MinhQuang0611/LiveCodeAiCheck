s = input()
count = 0
for ch in s:
    if ch.lower() == 'a' or ch.lower() == 'e' or ch.lower() == 'i' or ch.lower() == 'o' or ch.lower() == 'u':
        count += 1
print(count)