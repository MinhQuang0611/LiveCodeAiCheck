text = input()
kitudacbiet = [",", " ", ":"]

for i in text:
    if i not in kitudacbiet:
        text += i
print(text.title())