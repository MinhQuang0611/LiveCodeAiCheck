from itertools import groupby

def nen_chuoi():
        s = input().strip()
        sstr = []
        
        for key, group in groupby(s):
            
            count = len(list(group))
            
            sstr.append(f"{count}{key}")
        
        print("".join(sstr))
    
if __name__=="__main__":
      n = int(input())
      while(n > 0):
            n-=1
            nen_chuoi()