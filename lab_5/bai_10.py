str1 = input("Nhập chuỗi Str1: ")
str2 = input("Nhập chuỗi Str2: ")

max_sub = ""
for i in range(len(str1)):
    # Duyệt qua tất cả các vị trí kết thúc
    for j in range(i + 1, len(str1) + 1):
        sub = str1[i:j]
        
        if sub in str2 and len(sub) > len(max_sub):
            max_sub = sub

if max_sub:
    print(f"Chuỗi con chung dài nhất là: '{max_sub}'")
    print(f"Độ dài: {len(max_sub)}")
else:
    print("Không có chuỗi con chung.")