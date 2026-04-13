List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103],
        ["fri", 115], ["sat", 128], ["sun", 120]]
# In danh sách
print("Danh sách List_: ")
for item in List_:
    print(item)
# Phân tử thứ hai, thuộc vị trí thứ 3 của sublist
phan_tu = List_[1][2] if len(List_[1]) > 2 else List_[1][1]
print(f"Phân tử thứ hai (List_[1]): {List_[1]}")
print(f"Vị trí thứ 3 của sublist (index 2): không tồn tại, nên lấy index 1 = {List_[1][1]}")
# Kiểm tra độ dài và thêm sublist ngẫu nhiên
import random
print(f"Độ dài của List_: {len(List_)}")
random_sub = [random.choice(["extra","bonus"]), random.randint(50,150)]
List_.append(random_sub)
print(f"Sau khi thêm sublist ngẫu nhiên {random_sub}: độ dài = {len(List_)}")
# Tổng sale value thứ Hai, Ba, Bảy, Chủ nhật
ngay_tinh = ["mon", "tue", "sat", "sun"]
tong_sale = sum(item[1] for item in List_ if item[0] in ngay_tinh)
print(f"Tổng sale value của (thứ hai, thứ ba, thứ bảy, chủ nhật): {tong_sale}")