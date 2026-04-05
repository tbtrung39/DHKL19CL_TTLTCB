Str1 = input("Nhập chuỗi 1: ")
Str2 = input("Nhập chuỗi 2: ")
max_str = ""
for i in range(len(Str1)):
    for j in range(len(Str2)):
        temp = ""
        k = 0
        while (i + k < len(Str1)) and (j + k < len(Str2)) and (Str1[i + k] == Str2[j + k]):
            temp = temp + Str1[i + k]
            k = k + 1
        if len(temp) > len(max_str):
            max_str = temp
print("Chuỗi chung dài nhất là:", max_str)