import my_Square
def main():
    a = float(input("Nhap canh a: "))

    print("Chu vi hinh vuong: ", my_Square.ChuviHinhVuong(a))
    print("Dien tich hinh vuong: ", my_Square.DientichHinhVuong(a))

if __name__ == "__main__":
    main()