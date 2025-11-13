def countDigitOne(n):
    count = 0
    factor = 1  # Bắt đầu với vị trí đơn vị
    while factor <= n:
        lower_numbers = n - (n // factor) * factor  # Các số bên phải vị trí hiện tại
        current_digit = (n // factor) % 10  # Chữ số hiện tại
        higher_numbers = n // (factor * 10)  # Các số bên trái vị trí hiện tại
        
        # Tính số lượng '1' dựa trên giá trị của current_digit
        if current_digit == 0:
            count += higher_numbers * factor
        elif current_digit == 1:
            count += higher_numbers * factor + lower_numbers + 1
        else:
            count += (higher_numbers + 1) * factor
        
        factor *= 10  # Chuyển sang vị trí tiếp theo
    return count

n = int(input())

print(countDigitOne(n))