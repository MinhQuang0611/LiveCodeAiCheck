n = int(input())
cs = [int(ch) for ch in str(n)]
s = sum(cs)
mod = s % 3
if mod != 0:
    mod1 = [d for d in cs if d % 3 == 1]
    mod2 = [d for d in cs if d % 3 == 2]
    if mod == 1:
        if len(mod1) >= 1:
            cs.remove(min(mod1))
        elif len(mod2) >= 2:
            cs.remove(min(mod2))
            cs.remove(min(mod2))
        else:
            cs = []
    elif mod == 2:
        if len(mod2) >= 1:
            cs.remove(min(mod2))
        elif len(mod1) >= 2:
            cs.remove(min(mod1))
            cs.remove(min(mod1))
        else:
            cs = []
if not cs:
    print(-1)
else:
    cs.sort(reverse=True)
    if cs[0] == 0:
        print(0)
    else:
        ans = int("".join(str(d) for d in cs))
        print(ans)
