new_string = input()
string=[]
a=' '
b=','
c=':'
for i in new_string:
    if i.isalnum() or i == a or i == b or i == c:
        string.append(i)
print(((''.join(string)).replace('  ',' ', )).title())