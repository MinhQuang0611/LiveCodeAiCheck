t = int(input())
messages = []
for _ in range(t):
    message = input()
    message = message[:100]
    messages.append(message)
for msg in messages:
    print(msg)