def nhap_danh_sach():
    ds = []
    n = int(input("Nhap so luong nhan vien: "))
    for i in range(n):
        print(f"Nhap thong tin nhan vien thu {i+1}:")
        ma = input("Ma NV: ")
        ten = input("Ten NV: ")
        chucvu = input("Chuc vu (TP/PP/NV): ")
        he_so = float(input("He so luong: "))
        luong = he_so * 1490000
        if chucvu == "TP":
            phu_cap = 1000000
        elif chucvu == "PP":
            phu_cap = 700000
        else:
            phu_cap = 300000
        thuc_linh = luong + phu_cap
        nv = {
            "MaNV": ma,
            "TenNV": ten,
            "ChucVu": chucvu,
            "Hesoluong": he_so,
            "Luong": luong,
            "Phucap": phu_cap,
            "Thuclinh": thuc_linh
        }
        ds.append(nv)
    return ds

def hien_thi(ds):
    print("DANH SACH NHAN VIEN:")
    print("{:<10} {:<20} {:<10} {:<15} {:<15} {:<15} {:<15}".format(
        "MaNV", 
        "TenNV", 
        "ChucVu", 
        "Hesoluong", 
        "Luong", 
        "Phucap", 
        "Thuclinh"
        ))
    for nv in ds:
        print("{:<10} {:<20} {:<10} {:<15} {:<15} {:<15} {:<15}".format(
            nv["MaNV"],
            nv["TenNV"], 
            nv["ChucVu"], 
            nv["Hesoluong"], 
            nv["Luong"], 
            nv["Phucap"], 
            nv["Thuclinh"]
            ))
def sap_xep(ds):
    ds.sort(key=lambda x: x["Thuclinh"], reverse=True)

def luu_file(ds,ten_file):
    with open(ten_file, "w", encoding="utf-8") as file:
        file.write("MaNV,TenNV,ChucVu,Hesoluong,Luong,Phucap,Thuclinh\n")
        for nv in ds:
            dong = (
                f"{nv['MaNV']},"
                f"{nv['TenNV']},"
                f"{nv['ChucVu']},"
                f"{nv['Hesoluong']},"
                f"{nv['Luong']},"
                f"{nv['Phucap']},"
                f"{nv['Thuclinh']}\n"
            )
            file.write(dong)
            print("Da luu vao file:", ten_file)

