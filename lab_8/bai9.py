def may_tinh_co_ban(a, b):
    cong = a + b
    tru = a - b
    nhan = a * b
    chia = a / b if b != 0 else "Không thể chia cho 0"
    return cong, tru, nhan, chia

# Sử dụng hàm
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
co, tr, nh, ch = may_tinh_co_ban(a, b)

print(f"Cộng: {co} | Trừ: {tr} | Nhân: {nh} | Chia: {ch}")