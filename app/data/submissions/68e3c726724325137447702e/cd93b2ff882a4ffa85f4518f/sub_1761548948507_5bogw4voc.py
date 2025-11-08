s=input().strip()
count={}
for ch in s:
    count[ch]=count.get(ch,0)+1
if count.get("(",0)==count.get(")",0):
    print("true")
else:
    print("ValueError: Parentheses not balanced")
