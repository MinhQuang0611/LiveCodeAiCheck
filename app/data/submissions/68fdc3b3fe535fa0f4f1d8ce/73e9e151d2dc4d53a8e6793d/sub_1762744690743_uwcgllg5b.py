n = int(input())
_list = []
for _ in range(n):
    _str =  input()
    if _str != "-1":
        _list.append(_str)
print(len(set(_list)))