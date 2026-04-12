List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]

print(List_) # In danh sách
print(List_[2][1]) # Giá trị sale của phần tử thứ 3 (wed)

List_.append(["new", 100]) # Thêm phần tử ngẫu nhiên
print(len(List_)) # In độ dài

# Tính tổng sale các ngày cụ thể
target = ["mon", "tue", "sat", "sun"]
tong = sum(v for k, v in List_ if k in target)
print("Tổng sale:", tong)