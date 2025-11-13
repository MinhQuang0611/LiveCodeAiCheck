t=int(input())
a_i=[]
b_i=[]
ngon_nui=1
for so_bo in range(t):
    n=int(input())
    for nui in range(n):
        a,b=map(int,input().split())
        a_i+=[a]
        b_i+=[b]
so_nui=len(a_i)
for thu_tu_nui in range(so_nui-1):
        if a_i[thu_tu_nui]<a_i[thu_tu_nui+1] and b_i[thu_tu_nui]>b_i[thu_tu_nui+1]:
            ngon_nui+=1
print(ngon_nui)