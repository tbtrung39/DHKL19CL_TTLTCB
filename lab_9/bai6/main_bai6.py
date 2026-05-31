import doicoso2

chuoi_goc = input("Nhập chuỗi ký tự bất kỳ: ")
chuoi_xl = doicoso2.loai_bo_ky_tu_loi(chuoi_goc)
print(f"Chuỗi sau xử lý sạch: {chuoi_xl}")

if chuoi_xl:
    cs_doan = doicoso2.doan_co_so(chuoi_xl)
    print(f"Dự đoán chuỗi thuộc cơ số: {cs_doan}")
    
    print(f"Chuyển từ cơ số 2 -> 10: {doicoso2.sang_co_so_10(chuoi_xl, 2)}")
    print(f"Chuyển từ cơ số 8 -> 10: {doicoso2.sang_co_so_10(chuoi_xl, 8)}")
    print(f"Chuyển từ cơ số 16 -> 10: {doicoso2.sang_co_so_10(chuoi_xl, 16)}")
else:
    print("Chuỗi rỗng sau khi lọc!")