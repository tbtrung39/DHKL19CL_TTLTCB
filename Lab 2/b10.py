a = int(input("Nhập giờ bắt đầu thuê sân: "))
b = int(input("Nhập giờ kết thúc thuê sân: "))
if 5 <= a and b <= 22:
    h = b-a 
    if h <=3:
        tien = h * 100000
        print("Số tiền phải trả là: ",tien)
    elif h > 3: 
        gio_du = h - 3
        tien = (h * 100000 ) + gio_du * 75000
        print ("Tiền phải trả: ", tien)
    elif 11 <= a and b <= 15:
        tien = (h * 100000) * 0.9
        print("Số tiền phải trả là: ", tien)
else: 
    print("Chưa mở cửa cho thuê")