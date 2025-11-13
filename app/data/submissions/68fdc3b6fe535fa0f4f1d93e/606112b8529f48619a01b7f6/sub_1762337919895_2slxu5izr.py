t=int(input())
val=list(map(int,input().split()))
max_val=max(val)
min_val=min(val)
new_val=[x for x in val if x != max_val and x != min_val]
if len(new_val) == 0:
    print(f'{(sum(val)/len(val)):.0f}')
else:
    print(f'{(sum(new_val)/len(new_val)):.0f}')