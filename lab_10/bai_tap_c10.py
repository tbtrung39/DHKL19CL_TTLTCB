#Bài 7
import random
import math
def sinh_ngau_nhien(n):
    return[random.randint(1,100) for _ in range(n) ]
def so_nt(n):
    if n<=2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True   

def lke_chia_7(ds):
    for x in ds :
        if so_nt(x) and x%7==0:
            return x
        
def tinh_tong_le(danh_sach):
    return sum([x for x in danh_sach if x % 2 != 0])

def kiem_tra_chinh_phuong(danh_sach):
    def uoc_so_cp(num):
        if num < 0:
            return False
        root = int(math.sqrt(num))
        return root * root == num
    cac_so_cp = [x for x in danh_sach if uoc_so_cp(x)]
    return cac_so_cp    

n=int(input("nhập phần tử n "))
ds=sinh_ngau_nhien(n)
print("dãy so ngẫu nhiên là :",ds)
cac_so_t7 = lke_chia_7(ds)
print(f"Các số nguyên tố chia hết cho 7 trong dãy: {cac_so_t7}")
tong_le = tinh_tong_le(ds)
print(f"Tổng các số lẻ trong dãy: {tong_le}")
cac_so_cp = kiem_tra_chinh_phuong(ds)
if cac_so_cp:
    print(f"Trong dãy CÓ số chính phương. Các số đó là: {list(set(cac_so_cp))}")
else:
    print("Trong dãy KHÔNG có số chính phương nào.")

#Bài 8
def nhap_ma_tan(n):
    ma_tran=[]
    print(f"Nhập ma trận kích thước {n}x{n}")
    for i in range(n):
        hang=[]
        for j in range(n):
            gtri=float(input("Nhập phần tử :"))
            hang.append(gtri)
        ma_tran.append(hang)
    return ma_tran
def ma_tran_cv(ma_tran):
    n= len(ma_tran)
    cv=[[ma_tran[j][i] for j in range(n)] for i in range(n)]
    return cv
def ktr_doi_xung(ma_tran):
    n = len(ma_tran)
    for i in range(n):
        for j in range(i + 1, n):
            if ma_tran[i][j] != ma_tran[j][i]:
                return False
    return True
n=int(input("Nhập kích thước ma trận :"))
mt=nhap_ma_tan(n)
print("Ma trận vừa nhập là :",mt)
mt_cv=ma_tran_cv(mt)
print("Ma trận chuyển vị là :",mt_cv)
if ktr_doi_xung(mt):
    print("là ma trận dối xứng")
else:
    print("ko là mtran đối xứng")

#Bài 9
def nhap_ds():
    ds=[]
    while True :
        ma= input("Nhập mã:")
        if not ma:
            break
        ten=input("Nhập tên hang:").split()
        dvt=input("Nhập đơn vị:").split()
        don_gia=float(input("Nhập đơn giá:"))
        so_luong=float(input("Nhập số lượng:"))
        thanh_tien=don_gia*so_luong
        thue=thanh_tien*0.1
        mat_hang = {
            "ma_hang": ma,
            "ten_hang": ten,
            "dvt": dvt,
            "don_gia": don_gia,
            "so_luong": so_luong,
            "thanh_tien": thanh_tien,
            "thue": thue
        }
        ds.append(mat_hang)
    return ds
def in_danh_sach(danh_sach):
    if len(danh_sach) == 0:
        print("Danh sách trống.")
        return
        
    for h in danh_sach:
        print(f"Mã: {h['ma_hang']} | Tên: {h['ten_hang']} | SL: {h['so_luong']} {h['dvt']} | "
              f"Tiền: {h['thanh_tien']:,} | Thuế: {h['thue']:,}")
def sap_xep_theo_thue_giam_dan(danh_sach):
    n = len(danh_sach)
    ds_sap_xep = list(danh_sach)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ds_sap_xep[j]["thue"] < ds_sap_xep[j+1]["thue"]:
                tam = ds_sap_xep[j]
                ds_sap_xep[j] = ds_sap_xep[j+1]
                ds_sap_xep[j+1] = tam
                
    return ds_sap_xep        
ds_goc=nhap_ds()
print(ds_goc)
ds_sx=sap_xep_theo_thue_giam_dan(ds_goc)
print(ds_sx)
in_danh_sach(ds_sx)
print(in_danh_sach)
