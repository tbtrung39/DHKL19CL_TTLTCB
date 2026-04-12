str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")
ket_qua = ""
i = 0

while i < len(str1) and i < len(str2):
    ket_qua += str1[i] + str2[i]
    i += 1
ket_qua += str1[i:] + str2[i:]
print("Kết quả trộn:", ket_qua)