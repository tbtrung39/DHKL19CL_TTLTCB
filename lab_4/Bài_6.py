chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
n = input("Nhập một số: ")

ket_qua = ""
for so in n:
    if so.isdigit(): # Kiểm tra nếu là chữ số
        ket_qua += chu_so[int(so)] + " "

print("Kết quả:", ket_qua.strip())