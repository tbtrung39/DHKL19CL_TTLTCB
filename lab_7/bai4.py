chieu_cao_list = [
    161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163,
    162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170
]
#a
so_luong_sv = len(chieu_cao_list)
print(f"a. Nhóm có tổng cộng: {so_luong_sv} sinh viên.")
#b
chieu_cao_trung_binh = sum(chieu_cao_list) / so_luong_sv
print(f"b. Chiều cao trung bình của các sinh viên: {chieu_cao_trung_binh:.2f} cm")
#c
chieu_cao_khac_nhau = set(chieu_cao_list)
chieu_cao_sap_xep = sorted(chieu_cao_khac_nhau)

print("Các chiều cao khác nhau của sinh viên trong nhóm là:")
print(chieu_cao_sap_xep)
print(f"-> Có tất cả {len(chieu_cao_sap_xep)} mức chiều cao khác nhau.")
chieu_cao_trung_binh = sum(chieu_cao_list) / len(chieu_cao_list)
print(f"Chiều cao trung bình của nhóm sinh viên: {chieu_cao_trung_binh:.2f} cm")
