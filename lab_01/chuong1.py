import math #chuong1

# 1
def thong_tin_sinh_vien():
    ma_sv = input("Mã sinh viên: ")
    ho_ten = input("Họ tên: ")
    que_quan = input("Quê quán: ")
    nam_sinh = int(input("Năm sinh: "))
    diem_tb = float(input("Điểm trung bình: "))

    print("Thông tin sinh viên:")
    print("Mã SV:", ma_sv)
    print("Họ tên:", ho_ten)
    print("Quê quán:", que_quan)
    print("Năm sinh:", nam_sinh)
    print("Điểm TB:", diem_tb)


# 2
def doi_thoi_gian():
    s = int(input("Nhập số giây: "))

    d = s // 86400
    s %= 86400

    h = s // 3600
    s %= 3600

    m = s // 60
    s %= 60

    print(d, "ngày,", h, "giờ,", m, "phút,", s, "giây")


# 3
def tinh_khoi_tru():
    r = float(input("Bán kính: "))
    h = float(input("Chiều cao: "))
    pi = 3.14

    s_xq = 2*pi*r*h
    s_tp = 2*pi*r*(r+h)
    v = pi*r*r*h

    print("Diện tích xung quanh:", round(s_xq,2))
    print("Diện tích toàn phần:", round(s_tp,2))
    print("Thể tích:", round(v,2))


# 4
def gia_tri_bieu_thuc_1():
    x = float(input("Nhập x: "))

    tu = -x + math.sqrt(x**2 + 4)
    mau = (x**4 + 1)**(1/7)

    f = tu/mau

    print("f(x) =", round(f,2))


# 5
def tich_vo_huong_vector():
    a1 = float(input("a1="))
    a2 = float(input("a2="))
    a3 = float(input("a3="))

    b1 = float(input("b1="))
    b2 = float(input("b2="))
    b3 = float(input("b3="))

    tich = a1*b1 + a2*b2 + a3*b3

    print("Tích vô hướng:", tich)


# 6
def tien_dien_bong_den():
    t = int(input("Thời gian dùng (giây): "))

    p = 220 * 2.7
    kwh = (p * t) / (1000 * 3600)

    tien = kwh * 7000

    print("Tiền điện:", round(tien,2))


# 7
def giai_pt_bac_2():
    a = float(input("a="))
    b = float(input("b="))
    c = float(input("c="))

    delta = b*b - 4*a*c

    if delta < 0:
        print("Vô nghiệm")
    elif delta == 0:
        x = -b/(2*a)
        print("Nghiệm kép:", round(x,2))
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("x1 =", round(x1,2))
        print("x2 =", round(x2,2))


# 8
def trong_tam_tam_giac():
    x1,y1 = map(float,input("A (x y): ").split())
    x2,y2 = map(float,input("B (x y): ").split())
    x3,y3 = map(float,input("C (x y): ").split())

    x = (x1+x2+x3)/3
    y = (y1+y2+y3)/3

    print("Trọng tâm:", round(x,2), round(y,2))


# 9
def diem_doi_xung():
    x,y,z = map(float,input("Nhập điểm (x y z): ").split())

    print("Qua Oxy:", x, y, -z)
    print("Qua Oxz:", x, -y, z)
    print("Qua Oyz:", -x, y, z)


# 10
def gia_tri_bieu_thuc_log():
    x = float(input("Nhập x: "))

    f = math.log(x,4) + math.log(2,x)

    print("f(x) =", round(f,2))


# 11
def xac_suat_3_xuc_xac():
    n = int(input("Nhập số lần tung: "))

    p = 1 - (215/216)**n

    print("Xác suất:", round(p,2))


# 12
def van_toc_xe():
    a = float(input("Nhập a: "))
    t = float(input("Nhập t: "))

    v = -t * math.log(5,4) + a

    print("v(t) =", round(v,2))

thong_tin_sinh_vien()
doi_thoi_gian()
tinh_khoi_tru()
tich_vo_huong_vector()
gia_tri_bieu_thuc_1()
tien_dien_bong_den()   
giai_pt_bac_2()
trong_tam_tam_giac()
diem_doi_xung()
gia_tri_bieu_thuc_log()
xac_suat_3_xuc_xac()
van_toc_xe()