s = input()
s=''.join(c for c in s if c.isalnum() or c in ' ,:')
s=s.title()
print(s)
