from modules import pt_b1, pt_b2
def main():
    print("1. Giải phương trình bậc nhất ax + b = 0")
    print("2. Giải phương trình bậc hai ax^2 + bx + c = 0")
    choice = int(input("Chọn loại phương trình cần giải: "))
    if choice == 1:
        a = float(input("Nhập hệ số a: "))
        b = float(input("Nhập hệ số b: "))
        print(pt_b1(a, b))
    elif choice == 2:
        a = float(input("Nhập hệ số a: "))
        b = float(input("Nhập hệ số b: "))
        c = float(input("Nhập hệ số c: "))
        print(pt_b2(a, b, c))
    else:
        print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()