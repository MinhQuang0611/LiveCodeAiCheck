string = input()

dct = {}
new_string = ""
for index, ch in enumerate(string):
    if ch not in dct:
        dct[ch] = 1
    else:
        dct[ch] += 1

for index, ch in enumerate(string):
    if dct[ch] == 1:
        new_string += ch
    
print(new_string)

