def duyet():
    s = input()
    st = []
    id_mo = 1
    res = []
    for char in s:
        if char == '(':
            id_push = id_mo
            st.append(id_push)
            res.append(id_push)
            id_mo += 1
        elif char == ')':
            id_dong = st.pop()
            res.append(id_dong)
    print(*res)

if __name__=="__main__":
    n = int(input())
    while(n>0):
        n-=1
        duyet()