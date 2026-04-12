danh_sach = []

print("Nhập thông tin theo định dạng: Tên,Tuổi,Điểm (Để trống và nhấn Enter để dừng nhập):")
while True:
    chuoi_nhap = input()
    if not chuoi_nhap: 
        break
    thong_tin = chuoi_nhap.split(',')
    nguoi = (thong_tin[0].strip(), int(thong_tin[1].strip()), int(thong_tin[2].strip()))
    danh_sach.append(nguoi)
danh_sach.sort()
print("Danh sách sau khi sắp xếp:")
print(danh_sach)