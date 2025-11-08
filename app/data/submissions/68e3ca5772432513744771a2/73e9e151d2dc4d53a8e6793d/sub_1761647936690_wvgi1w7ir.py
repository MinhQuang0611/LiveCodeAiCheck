import ast
def kiem_tra_so_doi_xung(n: int, digits: list) -> bool:
    tap_hop_digits = set(digits) 
    chuoi_n = str(n)
    
    if chuoi_n != chuoi_n[::-1]:
        return False
        
    for ky_tu_chu_so in chuoi_n:
        chu_so = int(ky_tu_chu_so) 
        if chu_so not in tap_hop_digits:
            return False

    return True

number = int(input())
digit = ast.literal_eval(input())
print(kiem_tra_so_doi_xung(number, digit))