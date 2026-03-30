n = int(input("Nhập số lần tung n: "))

p_mot_lan = 1 / (6**3)
p_khong_lan_nao = (1 - p_mot_lan)**n
p_it_nhat_mot_lan = 1 - p_khong_lan_nao

print(f"Xác suất cần tìm: {round(p_it_nhat_mot_lan, 2)}")
#