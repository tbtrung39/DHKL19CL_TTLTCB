Str = input("Nhập chuỗi: ")
max_str = ""
current_str = Str[0]
for i in range(1, len(Str)):
    if Str[i] == current_str[-1]:
        current_str = current_str + Str[i]
    else:
        if len(current_str) > len(max_str):
            max_str = current_str
        current_str = Str[i]
if len(current_str) > len(max_str):
    max_str = current_str
print("Chuỗi dài nhất là:", max_str)