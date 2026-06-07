import doicoso.doicoso1 as d1
import doicoso.doicoso2 as d2


def main():
    print('--- Chuyển cơ số (dùng doicoso1) ---')
    n = int(input('Nhập số nguyên dương: '))
    print('1. Nhị phân  2. Bát phân  3. Thập lục')
    c = int(input('Chọn: '))
    if c == 1:
        d1.convert_to_binary(n)
    elif c == 2:
        d1.convert_to_octal(n)
    elif c == 3:
        d1.convert_to_hexadecimal(n)
    else:
        print('Lựa chọn không hợp lệ')

    print('\n--- Phân tích chuỗi (dùng doicoso2) ---')
    s = input('Nhập chuỗi số/hex: ').upper()
    print('Phát hiện hệ:', d2.detect_hecoso(s))
    print(d2.convert_binary_to_decimal(s))
    print(d2.convert_octal_to_decimal(s))
    print(d2.convert_hexadecimal_to_decimal(s))


if __name__ == '__main__':
    main()
