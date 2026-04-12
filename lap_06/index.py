import random

def cau_1():
    a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
    tong = 0
    for i in a:
        tong += i
    print("Tong cac phan tu trong mang la: ", tong)

    dem_duong = 0
    tong_duong = 0
    for i in a:
        if i > 0:
            dem_duong += 1
            tong_duong += i
    print("Tong cac phan tu duong trong mang la: ", tong_duong)
    print("So luong phan tu duong trong mang la: ", dem_duong)

    vi_tri_am_dau_tien = -1
    for i in range(len(a)):
        if a[i] < 0:
            vi_tri_am_dau_tien = i
            break
    if vi_tri_am_dau_tien != -1:
        print("Vi tri phan tu am dau tien trong mang la: ", vi_tri_am_dau_tien)
    else:
        print("Khong co phan tu am trong mang.")

    vi_tri_duong_cuoi_cung = -1
    for i in range(len(a) - 1, -1, -1):
        if a[i] > 0:
            vi_tri_duong_cuoi_cung = i
            break
    if vi_tri_duong_cuoi_cung != -1:
        print("Vi tri phan tu duong cuoi cung trong mang la: ", vi_tri_duong_cuoi_cung)
    else:
        print("Khong co phan tu duong trong mang.")

    max_value = a[0]
    max_index = 0
    for i in range(1, len(a)):
        if a[i] > max_value:
            max_value = a[i]
            max_index = i
    print("Phan tu lon nhat trong mang la: ", max_value)
    print("Vi tri cua phan tu lon nhat trong mang la: ", max_index)

def cau_2():
    n = []
    while True:
        x = input("Nhap so nguyen (nhap q de thoat): ")
        if x == 'q':
            break
        n.append(int(x))

    b = [x for x in n if x % 3 == 0 and x % 5 != 0]
    print("Cac so chia het cho 3 nhung khong chia het cho 5: ", b)

    c = [x**2 for x in n]
    print("Cac phan tu la binh phuong cua danh sach n: ", c)

    d = [x for x in n if x % 3 == 0]
    if len(d) > 0:
        random_element = random.choice(d)
        print("Phan tu ngau nhien trong danh sach n ma chia het cho 3: ", random_element)
    else:
        print("Khong co phan tu nao trong danh sach n ma chia het cho 3.")

def cau_3():
    balance = 0
    while True:
        print("Nhập giao dịch (D cho nạp tiền, W cho rút tiền): ")
        entry = input("Nhập giao dịch (Enter để dừng): ")
        if entry == "":
            break
        loai, so_tien = entry.split()
        so_tien = int(so_tien)
        if loai == "D":
            balance += so_tien
        elif loai == "W":
            balance -= so_tien
    print("Số dư tài khoản:", balance)

def cau_4():
    chu_ngu = ["Anh", "Em"]
    dong_tu = ["Chơi", "Yêu"]
    tan_ngu = ["Bóng đá", "Bóng rổ"]
    cau = [f"{cn} {dt} {tn}" for cn in chu_ngu for dt in dong_tu for tn in tan_ngu]
    for x in cau:
        print(x)

def cau_5():
    chuoi = input("Nhập các mật khẩu (cách nhau bởi dấu phẩy): ")
    danh_sach = [p.strip() for p in chuoi.split(",")]
    hop_le = [p for p in danh_sach if
              any(c.islower() for c in p) and
              any(c.isdigit() for c in p) and
              any(c.isupper() for c in p) and
              any(c in "$#@" for c in p) and
              6 <= len(p) <= 12]
    print("Mật khẩu hợp lệ:", ",".join(hop_le))

def cau_6():
    n = int(input("Nhập số người: "))
    data = []
    for i in range(n):
        name = input("Tên: ")
        age = int(input("Tuổi: "))
        score = float(input("Điểm: "))
        data.append((name, age, score))
    data.sort(key=lambda x: (x[0], x[1], x[2]))
    print("Sau khi sắp xếp:", data)

def cau_7():
    X = int(input("Nhập X: "))
    Y = int(input("Nhập Y: "))
    mang = [[i * j for j in range(Y)] for i in range(X)]
    print("Mảng 2 chiều:", mang)

def cau_8():
    n = int(input("Nhập n: "))
    don_vi = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for row in don_vi:
        print(row)

def cau_9():
    m = int(input("Nhập số hàng m: "))
    n = int(input("Nhập số cột n: "))
    A = [[int(input(f"a[{i+1}][{j+1}]: ")) for j in range(n)] for i in range(m)]
    print("Ma trận A:")
    for row in A:
        print(row)
    tong = sum(A[i][j] for i in range(m) for j in range(n))
    print("Tổng các phần tử:", tong)

def cau_10():
    n = []
    while True:
        x = input("Nhap so nguyen (nhap q de thoat): ")
        if x == 'q':
            break
        n.append(int(x))

    if len(n) < 2:
        print("Khong co phan tu lon thu 2 trong mang.")
    else:
        max_value = n[0]
        second_max_value = 0
        max_index = 0
        second_max_index = 0
        for i in range(1, len(n)):
            if n[i] > max_value:
                second_max_value = max_value
                second_max_index = max_index
                max_value = n[i]
                max_index = i
            elif n[i] > second_max_value and n[i] != max_value:
                second_max_value = n[i]
                second_max_index = i
        if second_max_value == 0:
            print("Khong co phan tu lon thu 2 trong mang.")
        else:
            print("Phan tu lon thu 2 trong mang la: ", second_max_value)
            print("Vi tri cua phan tu lon thu 2 trong mang la: ", second_max_index)

    max_count = 0
    current_count = 0
    for i in range(len(n)):
        if n[i] > 0:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    print("So luong cac so nguyen duong lien tiep trong mang la: ", max_count)

    max_sum = 0
    current_sum = 0
    current_count = 0
    for i in range(len(n)):
        if n[i] > 0:
            current_sum += n[i]
            current_count += 1
            if current_sum > max_sum:
                max_sum = current_sum
                max_count = current_count
        else:
            current_sum = 0
            current_count = 0
    print("So luong cac so duong lien tiep co tong lon nhat trong mang la: ", max_count)

def cau_11():
    n = []
    while True:
        x = int(input("Nhap so tu nhien (nhap 0 de thoat): "))
        if x == 0:
            break
        n.append(x)

    duong = []
    am = []
    for i in n:
        if i > 0:
            duong.append(i)
        else:
            am.append(i)
    n = duong + am
    print("Danh sach sau khi chuyen cac phan tu duong len dau: ", n)

    m = int(input("Nhap so m: "))
    n.insert(0, m)
    n.append(m)
    if len(n) >= 5:
        n.insert(4, m)
    print("Danh sach sau khi chen so m vao dau, cuoi va vi tri thu 5: ", n)

def cau_12():
    n = []
    while True:
        x = int(input("Nhap so tu nhien (nhap 0 de thoat): "))
        if x == 0:
            break
        n.append(x)

    n = [1, 2, 3] + n
    print("Danh sach sau khi chen [1,2,3] vao dau: ", n)

    n = n + [1, 2, 3]
    print("Danh sach sau khi chen [1,2,3] vao cuoi: ", n)

    if len(n) >= 5:
        n = n[:4] + [1, 2, 3] + n[4:]
    print("Danh sach sau khi chen [1,2,3] vao vi tri thu 5: ", n)

    k = int(input("Nhap so k can xoa: "))
    if k in n:
        n.remove(k)
        print("Danh sach sau khi xoa phan tu k: ", n)
    else:
        print("Khong co phan tu k trong danh sach.")

    for i in range(len(n) - 1):
        for j in range(i + 1, len(n)):
            if n[i] > n[j]:
                n[i], n[j] = n[j], n[i]
    print("Danh sach sau khi sap xep tang dan: ", n)

    for i in range(len(n) - 1):
        for j in range(i + 1, len(n)):
            if n[i] < n[j]:
                n[i], n[j] = n[j], n[i]
    print("Danh sach sau khi sap xep giam dan: ", n)

def cau_13():
    n = []
    for i in range(1000):
        n.append(random.randint(1, 99999))
    print("Danh sach 1000 so tu nhien: ", n)

def cau_14():
    n = []
    for i in range(1000):
        n.append(random.randint(1, 99999))
    print("Danh sach 1000 so tu nhien: ", n)

    n_sorted = sorted(n)
    print("Danh sach sau khi sap xep tang dan: ", n_sorted)

    for i in range(len(n) - 1):
        for j in range(i + 1, len(n)):
            if n[i] > n[j]:
                n[i], n[j] = n[j], n[i]
    print("Danh sach sau khi sap xep tang dan: ", n)

def cau_15():
    List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
    for i in List_:
        print(i)

    print("Phan tu thu 2 cua sublist thu 3 la: ", List_[2][1])
    print("Do dai cua List_ la: ", len(List_))

    new_sublist = ["new_day", random.randint(1, 150)]
    List_.append(new_sublist)
    print("List_ sau khi them sublist moi la: ", List_)

    total_sale = List_[1][1] + List_[2][1] + List_[6][1] + List_[7][1]
    print("Tong sale value cua List_ trong thu 2,3,7 ,cn la: ", total_sale)

def cau_16():
    n = int(input("Nhap so n: "))
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    print("Day Fibonacci: ", ", ".join(str(x) for x in fibonacci[:n]))

def cau_17():
    n = []
    while True:
        x = input("Nhap so (nhap q de thoat): ")
        if x == 'q':
            break
        n.append(int(x))
    assert all(x % 2 == 0 for x in n), "Tat ca cac so phai la chan"
    print("Tat ca cac so trong list n la chan.")

if __name__ == "__main__":
    cau_1()
    cau_2()
    cau_3()
    cau_4()
    cau_5()
    cau_6()
    cau_7()
    cau_8()
    cau_9()
    cau_10()
    cau_11()
    cau_12()
    cau_13()
    cau_14()
    cau_15()
    cau_16()
    cau_17()
