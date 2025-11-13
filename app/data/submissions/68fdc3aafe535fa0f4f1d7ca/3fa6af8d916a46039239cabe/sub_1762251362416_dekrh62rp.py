s=input()
s="".join(reversed(s))
new=""
for i in range(0,len(s),3):
    new+=s[i:i+3]+","
s="".join(reversed(new[:len(new)-1]))
print(s)