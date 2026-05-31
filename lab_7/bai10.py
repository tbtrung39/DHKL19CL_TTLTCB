m = input("Nhập số tự nhiên m: ")
n = input("Nhập số tự nhiên n: ")
set_m = set(m)
set_n = set(n)
chu_so_chung = set_m & set_n
tong = sum(int(chong) for chong in chu_so_chung)

print("Các chữ số chung:", chu_so_chung)
print("Tổng các chữ số chung:", tong)