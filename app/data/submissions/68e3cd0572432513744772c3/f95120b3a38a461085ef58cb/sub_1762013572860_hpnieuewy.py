n = input()
a = False
for i in range(len(n)):
    if n[i] in n[i+1:]:
        a = True
        break
if a:
    print("true")
else:
    print("false")