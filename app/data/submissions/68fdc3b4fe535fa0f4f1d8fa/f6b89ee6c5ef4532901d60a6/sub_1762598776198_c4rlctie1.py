import math 
def snt(n): #tìm số nguyên tố
    if n<2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n %i ==0: 
            return False
    return True

def sap_xep_snt(nums): #sắp xếp snt
    vi_tri=[]
    gia_tri=[]
#Hàm enumerate cho phép chúng ta truy cập cả chỉ số và giá trị của các phần tử trong List      
    for i, num in enumerate(nums):
         if snt(num):   
            vi_tri.append(i)     
            gia_tri.append(num)
    gia_tri.sort()
    for j in range(len(vi_tri)):
        nums[vi_tri[j]]=gia_tri[j]
    return nums
n= int(input())
nums=list(map(int, input().split()))
print(*sap_xep_snt(nums))   