def binary_to_octal(binary_str):
    a  = 3 - len(binary_str)%3 
    new_n = '0'*a + binary_str 
    oct_final = ''
    for i in range(0,len(new_n),3):  
        oct_count = new_n[i:i+3]
        oct_digit = str(int(oct_count,2))
        oct_final += oct_digit 
    print(oct_final)
if __name__ == '__main__':
    binary_str = input()
    binary_to_octal(binary_str)