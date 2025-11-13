t=int(input())
def compress(s):
    if not s:
        return""
    result=[]
    count=1
    prev=s[0]
    for x in s[1:]:
        if x == prev:
            count +=1
        else:
            result.append(f"{count}{prev}") 
            prev= x
            count =1
    result.append(f"{count}{prev}")
    return"".join(result)
for _ in range(t):
    s=input().strip()
    print(compress(s))
