import hinhhoc.my_Triage as my_Triage
import hinhhoc.my_square as my_square


def main():
    print('=== HINH VUONG ===')
    a = float(input('Nhap canh hinh vuong a: '))
    print('Chu vi hinh vuong:', my_square.ChuviHinhVuong(a))
    print('Dien tich hinh vuong:', my_square.DientichHinhVuong(a))

    print('\n=== TAM GIAC ===')
    x = float(input('Nhap canh x: '))
    y = float(input('Nhap canh y: '))
    z = float(input('Nhap canh z: '))
    if my_Triage.is_TamGiac(x, y, z):
        print('Day la tam giac')
        print('Chu vi tam giac:', my_Triage.chuVi(x, y, z))
        print('Dien tich tam giac:', my_Triage.S_TamGiac(x, y, z))
    else:
        print('Khong phai tam giac')


if __name__ == '__main__':
    main()
