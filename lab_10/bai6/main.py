import doicoso2

chuoi_goc = input("Nhap chuoi ky tu: ")
chuoi_sach = doicoso2.loc_chuoi(chuoi_goc)

print(doicoso2.doan_co_so(chuoi_sach))

try:
    print(f"Tu co so 2 sang 10: {doicoso2.nhi_phan_sang_thap_phan(chuoi_sach)}")
except ValueError:
    print("Chuoi khong phai he co so 2 hop le!")

try:
    print(f"Tu co so 16 sang 10: {doicoso2.thap_luc_sang_thap_phan(chuoi_sach)}")
except ValueError:
    print("Chuoi khong phai he co so 16 hop le!")