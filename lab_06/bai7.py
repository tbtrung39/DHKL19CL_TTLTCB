List_ = [["mon", 73], ["tue", 89], ["wed", 95],["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
# In list
for x in List_:
    print(x)
# Chọn ra phần tử thứ 2 thuộc vị trí thứ 3 của sublist
print(List_[2][1])
# Thêm sublis
import random
test = List_.copy()
sub = ["new", random.randint(50,150)]
test.append(sub)
print(test)
# Tổng else value trong các ngày thứ hai, thứ 3, thứ 7, và chủ nhật
tong = 0
for x in List_:
    if x[0] in ["mon", "tue", "sat", "sun"]:
        tong += x[1]
print("Tổng: ", tong)
