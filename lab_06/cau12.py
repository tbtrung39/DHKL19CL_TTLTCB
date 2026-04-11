balance = 0

while True:
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