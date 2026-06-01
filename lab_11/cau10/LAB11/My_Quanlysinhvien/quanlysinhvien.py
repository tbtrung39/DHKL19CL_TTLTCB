def nhap_danh_sach():
    ds = []
    n = int(input("Nhap so luong sinh vien: "))
    for i in range(n):
        print(f"Nhap sinh vien thu {i + 1}")
        ma = input("Ma SV: ")
        ten = input("Ho ten: ")
        tb = float(input("Diem TB: "))
        rl = float(input("Diem RL: "))
        tl = (tb + rl) / 2
        sv = {
            "MaSV": ma,
            "HoTen": ten,
            "TB": tb,
            "RL": rl,
            "TL": tl
        }
        ds.append(sv)
    return ds

def hien_thi(ds):
    print("DANH SACH SINH VIEN")
    print("{:<10}{:<20}{:<10}{:<10}{:<10}".format(
        "MaSV",
        "HoTen",
        "TB",
        "RL",
        "TL"
    ))
    for sv in ds:
        print("{:<10}{:<20}{:<10.2f}{:<10.2f}{:<10.2f}".format(
            sv["MaSV"],
            sv["HoTen"],
            sv["TB"],
            sv["RL"],
            sv["TL"]
        ))


def sap_xep(ds):
    ds.sort(key=lambda x: x["RL"])

def tim_max_tl(ds):
    max_sv = ds[0]
    for sv in ds:
        if sv["TL"] > max_sv["TL"]:
            max_sv = sv
    return max_sv

def luu_file(ds, ten_file):
    with open(ten_file, "w", encoding="utf-8") as file:
        file.write("MaSV,HoTen,TB,RL,TL\n")
        for sv in ds:
            dong = (
                f"{sv['MaSV']},{sv['HoTen']},{sv['TB']},{sv['RL']},{sv['TL']}\n"
            )
            file.write(dong)
    print("Da luu file thanh cong!")