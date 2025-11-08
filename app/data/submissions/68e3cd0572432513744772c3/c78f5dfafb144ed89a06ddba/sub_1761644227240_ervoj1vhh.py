n = input()
a=list(n)
for i in range(len(a)):
    if a[i] == a[i+1]:
        print("true")
        found = True
        break
if not found:
    print("false")