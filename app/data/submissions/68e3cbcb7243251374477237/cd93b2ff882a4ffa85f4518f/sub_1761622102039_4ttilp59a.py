def ha(s: str):
    k=0
    mod=10**9+7
    for ch in s:
        k=(k+ord(ch))%mod
    return k
s=input()
print(ha(s))