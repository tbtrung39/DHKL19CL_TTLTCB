n = int(input("Nhập số lần tung (n): "))
p_mot_lan = (1/6)**3
xac_suat = 1 - (1 - p_mot_lan)**n
print(f"Xác suất ít nhất 1 lần cả 3 ra 6 là: {round(xac_suat, 2)}")