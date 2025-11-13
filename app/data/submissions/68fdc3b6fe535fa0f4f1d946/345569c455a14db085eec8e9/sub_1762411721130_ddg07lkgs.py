import re
a =input()
new_a = re.sub(r'[^A-Za-z0-9:, ]','',a)
new_a = ' '.join(new_a.split())
print(new_a.title())