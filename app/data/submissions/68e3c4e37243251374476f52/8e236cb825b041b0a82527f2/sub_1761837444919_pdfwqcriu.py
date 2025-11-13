from collections import Counter

ls = list(map(int, input()[1:-1].split(",")))
counter = Counter(ls)
new_ls = sorted(ls, key=lambda x: (-counter[x], x))
print("[" + ",".join(map(str, new_ls)) + "]")