n = int(input("Nhap so co 3 chu so: "))
tram = n // 100
chuc = (n % 100) // 10
donvi = n % 10
so = ["khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]
print(so[tram], "trăm", so[chuc], "muoi", so[donvi])
