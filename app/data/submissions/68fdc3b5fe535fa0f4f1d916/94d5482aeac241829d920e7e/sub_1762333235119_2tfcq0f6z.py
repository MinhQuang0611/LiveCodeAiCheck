from itertools import groupby

def nen_chuoi():
        s = input()
        str = []
        
        for key, group in groupby(s):
            
            count = len(list(group))
            
            str.append(f"{count}{key}")
        
        print("".join(str))
    
if __name__=="__main__":
    n = int(input())
    while(n > 0):
        n-=1
        nen_chuoi()