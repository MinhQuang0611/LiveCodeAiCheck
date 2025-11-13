a = int(input())
n = list(map(int, input().split()))
b = min(n)
c = max(n)
n = [x for x in n if x!=b]
n = [y for y in n if y!=c]
trung_binh=sum(n)//len(n)
print(trung_binh)