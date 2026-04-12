List_ = [["mon", 73], ["tue", 89], ["wed", 95],
         ["thu", 103], ["fri", 115], ["sat", 128],
         ["sun", 120]]

for item in List_:
    print(item)

print(List_[2][1])
print("Độ dài:", len(List_))
List_.append(["new", 100])
print(List_)

tong = List_[1][1] + List_[2][1] + List_[5][1] + List_[6][1]
print("Tổng:", tong)