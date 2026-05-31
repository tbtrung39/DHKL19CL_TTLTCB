char_set = set()
print("Nhập các ký tự(Nhấn ENTER để dừng lại): ")
while True:
    char = input("Nhập ký tự: ")
    if char == "":
        break
    if len(char) > 0:
        char_set.add(char[0])
print("Tập hợp ban đầu: ",char_set)
filtered_set = {ch for ch in char_set if not ch.isdigit()}
print("Tập hợp sau khi xóa kệ số:", filtered_set)