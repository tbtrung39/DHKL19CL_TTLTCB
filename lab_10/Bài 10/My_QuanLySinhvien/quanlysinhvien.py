# bài 10:
def nhap_danh_sach():
    n = int(input("Nhập số lượng sinh viên: "))
    ds = []
    for i in range(n):
        print(f"\nSinh viên {i+1}:")
        msv = input("Mã SV: ")
        ten = input("Họ tên: ")
        tb = float(input("Điểm TB: "))
        rl = float(input("Điểm RL: "))
        tl = (tb + rl) / 2
        ds.append({"MSV": msv, "Ten": ten, "TB": tb, "RL": rl, "TL": tl})
    return ds

def in_danh_sach(ds):
    print(f"\n{'MSV':<10} {'Họ tên':<20} {'TB':<5} {'RL':<5} {'TL':<5}")
    for sv in ds:
        print(f"{sv['MSV']:<10} {sv['Ten']:<20} {sv['TB']:<5} {sv['RL']:<5} {sv['TL']:<5.2f}")