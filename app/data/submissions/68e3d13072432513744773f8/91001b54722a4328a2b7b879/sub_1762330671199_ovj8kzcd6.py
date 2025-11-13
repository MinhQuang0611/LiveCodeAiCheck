import re
paragraph = input().strip()
banned = input().strip().split()
paragraph = paragraph.lower()
paragraph = re.sub(r'[^a-z\s]', ' ', paragraph)
words = paragraph.split()
counts = {}
for word in words:
    if word not in banned:
        counts[word] = counts.get(word, 0) + 1
most_common = max(counts, key=counts.get)
print(most_common)
