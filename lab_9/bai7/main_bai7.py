import xulidayso

day = xulidayso.tao_day_ngau_nhien()
print(f"Dãy số ngẫu nhiên được tạo:\n{day}\n")
print(f"Các số NT chia hết cho 7: {xulidayso.snt_chia_het_7(day)}")
print(f"Tổng các số lẻ: {xulidayso.tinh_tong_le(day)}")

scp = xulidayso.kiem_tra_so_chinh_phuong(day)
if scp:
    print(f"Các số chính phương trong dãy: {scp}")
else:
    print("Không có số chính phương trong dãy.")
