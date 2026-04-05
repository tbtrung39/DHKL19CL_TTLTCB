str = input(" nhap chuoi : ")
max_str = ""
current_str = ""
for i in range(len(str)):
    if i == 0 or str[i] == str[i - 1]:
        current_str += str[i]
    else: 
        current_str = str[i]
    if len(current_str) > len(max_str):
        max_str = current_str
print("Chuỗi con dài nhất có các ký tự giống nhau là:", max_str)