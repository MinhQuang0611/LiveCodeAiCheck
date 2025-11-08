a = input()
vowels='aeiou'
count=0
for ch in a.lower():
    if ch in vowels:
        count+=1
print(count)