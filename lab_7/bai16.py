# Giả định dữ liệu đầu vào cho 2 danh sách cùng độ dài n
list1 = [101, 102, 103, 104]
list2 = ["An", "Bình", "Cường", "Dương"]

# Cách 1: Sử dụng hàm zip() cực kỳ ngắn gọn và phổ biến trong Python
dictionary_zip = dict(zip(list1, list2))
print("Cách 1 (Dùng zip):", dictionary_zip)

# Cách 2: Sử dụng vòng lặp cơ bản theo chỉ số index
dictionary_loop = {}
for i in range(len(list1)):
    dictionary_loop[list1[i]] = list2[i]
    
print("Cách 2 (Dùng vòng lặp):", dictionary_loop)