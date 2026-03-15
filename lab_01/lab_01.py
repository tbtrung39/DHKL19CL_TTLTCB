import math

# --- ĐỊNH NGHĨA CÁC HÀM ---

def bai_1():
    a = input("Nhập mã sinh viên: ")
    b = input("Nhập họ tên: ")
    c = input("Nhập quê quán: ")
    d = int(input("Nhập năm sinh: "))
    e = float(input("Nhập điểm trung bình: "))
    print("\nTHÔNG TIN SINH VIÊN")
    print(f"Mã SV: {a}\nHọ tên: {b}\nQuê quán: {c}\nNăm sinh: {d}\nĐiểm TB: {e}")

def bai_2():
    s = int(input("Nhập số giây: "))
    a = s // 86400 # ngày
    s %= 86400
    b = s // 3600  # giờ
    s %= 3600
    c = s // 60    # phút
    d = s % 60     # giây
    print(f"Kết quả: {a} ngày, {b} giờ, {c} phút, {d} giây")

def bai_3():
    x = float(input("Nhập x: "))
    f = (-x + math.sqrt(x**2 + 4)) / ((x**4 + 1) ** (1/7))
    print("Giá trị f(x) =", round(f, 2))

def bai_4():
    print("Nhập vector a:")
    a1, a2, a3 = float(input("a1 = ")), float(input("a2 = ")), float(input("a3 = "))
    print("Nhập vector b:")
    b1, b2, b3 = float(input("b1 = ")), float(input("b2 = ")), float(input("b3 = "))
    sum_val = a1*b1 + a2*b2 + a3*b3
    print("Tích vô hướng =", sum_val)

def bai_5():
    u, i = 220, 2.7
    t = float(input("Nhập thời gian sử dụng (giây): "))
    p = u * i
    a = (p * t) / (1000 * 3600) # điện năng kWh
    sum_money = a * 7000
    print("Tiền điện phải trả =", round(sum_money, 2), "đ")

def bai_6():
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    d = b**2 - 4*a*c # delta
    if d < 0:
        print("Phương trình vô nghiệm")
    elif d == 0:
        print("Nghiệm kép x =", round(-b/(2*a), 2))
    else:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        print(f"x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")

def bai_7():
    x1, y1 = float(input("xA = ")), float(input("yA = "))
    x2, y2 = float(input("xB = ")), float(input("yB = "))
    x3, y3 = float(input("xC = ")), float(input("yC = "))
    a = (x1 + x2 + x3) / 3 # xG
    b = (y1 + y2 + y3) / 3 # yG
    print("Trọng tâm G =", (round(a, 2), round(b, 2)))

def bai_8():
    x, y, z = float(input("x = ")), float(input("y = ")), float(input("z = "))
    print(f"Đối xứng qua Oxy: {(x, y, -z)}")
    print(f"Đối xứng qua Oxz: {(x, -y, z)}")
    print(f"Đối xứng qua Oyz: {(-x, y, z)}")

def bai_9():
    x = float(input("Nhập x: "))
    f = math.log(x, 4) + math.log(2, x)
    print("f(x) =", round(f, 2))

def bai_10():
    n = int(input("Nhập số lần tung xúc xắc: "))
    p = 1 - (5/6)**n
    print("Xác suất =", round(p, 2))

def bai_11():
    a = float(input("Nhập vận tốc ban đầu: "))
    t = (a**4) / (math.log(5, 4))
    print("Thời gian xe dừng =", round(t, 2))

# --- GỌI CÁC HÀM CHẠY ---

if __name__ == "__main__":
    # Bạn có thể comment bớt các hàm không muốn chạy để test từng bài
    bai_1()
    bai_2()
    bai_3()
    bai_4()
    bai_5()
    bai_6()
    bai_7()
    bai_8()
    bai_9()
    bai_10()
    bai_11()
