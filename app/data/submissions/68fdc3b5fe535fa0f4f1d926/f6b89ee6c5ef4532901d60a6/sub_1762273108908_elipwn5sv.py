import itertools
n=int(input())
for _ in range(n):
    num=input().strip()
    nums=list(range(1, int(num)+1))
    list_hoan_vi=sorted(itertools.permutations(nums), reverse=True)
    print(len(list_hoan_vi))
    for p in list_hoan_vi:
        res= "".join(map(str, p))
        print(res, end=" ")
    print()
    
    
