from doicoso1 import *

def main():
    n = int(input("Nhập một số nguyên dương: "))
    print("Chọn hệ cơ số để chuyển đổi:")
    print("1. Hệ nhị phân")
    print("2. Hệ bát phân")
    print("3. Hệ thập lục phân")
    choice = int(input("Lựa chọn của bạn: "))
    if choice == 1:
        convert_to_binary(n)
    elif choice == 2:
        convert_to_octal(n)
    elif choice == 3:
        convert_to_hexadecimal(n)
    else:
        print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()