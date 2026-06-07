import sohoc
def main():
    a = int(input("Nhap so a: "))
    b = int(input("Nhap so b: "))

    print("Uoc chung lon nhat cua a va b: ", sohoc.Ucln(a, b))
    print("Boi chung nho nhat cua a va b: ", sohoc.Bscn(a, b))
    print("Tong cac uoc cua a: ", sohoc.SumDivisor(a))
    print("Tong cac uoc cua b: ", sohoc.SumDivisor(b))

if __name__ == "__main__":
    main()