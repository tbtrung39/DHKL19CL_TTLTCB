import sys
sys.path.append('lab_10\\Bai1\\')
import my_Triange

def main():
    a = float(input("Nhap canh a: "))
    b = float(input("Nhap canh b: "))
    c = float(input("Nhap canh c: "))

    if my_Triange.is_TamGiac(a, b, c):
        print("Day la 3 canh cua 1 tam giac.")
        print("Chu vi tam giac: ", my_Triange.chuVi(a, b, c))
        print("Dien tich tam giac: ", my_Triange.S_TamGiac(a, b, c))
    else:
        print("Day khong phai la 3 canh cua 1 tam giac.")

if __name__ == "__main__":
    main()