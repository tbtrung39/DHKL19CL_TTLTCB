str1 = input("Nhập chuỗi1: ")
str2 = input("Nhập chuỗi2: ")

max_char = ""
max_count = 0

for char in set(str1):
    if char in str2:
        count = str1.count(char) + str2.count(char)

        if count > max_count:
            max_count = count
            max_char = char
if max_char != "":
    print("Ký tự xuất hiện nhiều nhất trong cả hai chuỗi là:", max_char)
    print("Số lần xuất hiện của ký tự đó trong cả hai chuỗi là:", max_count)
else:
    print("Không có ký tự nào xuất hiện trong cả hai chuỗi.")
