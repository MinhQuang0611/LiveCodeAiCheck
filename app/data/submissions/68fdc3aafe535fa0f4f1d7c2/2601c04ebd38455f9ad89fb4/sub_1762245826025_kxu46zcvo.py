chuoi = input("Nhập chuỗi số có độ dài chẵn: ").strip()
cap_so = [chuoi[i:i+2] for i in range(0, len(chuoi), 2)]
cap_so_khac_nhau = sorted(set(cap_so), key=lambda x: int(x))
print("Các cặp số khác nhau theo thứ tự tăng dần là:")
print(*cap_so_khac_nhau)