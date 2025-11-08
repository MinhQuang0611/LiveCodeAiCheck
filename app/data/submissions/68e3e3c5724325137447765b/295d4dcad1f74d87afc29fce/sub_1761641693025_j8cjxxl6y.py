n=input()
sum= 0
for i in range(len(n)):
    if n[i].isdigit():
        number= int(n[i])
        sum += number
print(sum)