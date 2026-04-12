balance = 0

while True:
    print("Nhập giao dịch (D cho nạp tiền, W cho rút tiền): ")
    entry = input("Nhập giao dịch (Enter để dừng): ")
    if entry == "":
        break
    
    loai, so_tien = entry.split()
    so_tien = int(so_tien)
    
    if loai == "D":
        balance += so_tien
    elif loai == "W":
        balance -= so_tien

print("Số dư tài khoản:", balance)