chuoi_A = input("Nhập các ký tự cho tập hợp A (viết liền): ")
chuoi_B = input("Nhập các ký tự cho tập hợp B (viết liền): ")
A = set(chuoi_A)
B = set(chuoi_B)

print("Tập hợp A:", A)
print("Tập hợp B:", B)
phan_tu_chung = A & B  
print("Các phần tử chung của A và B:", phan_tu_chung)