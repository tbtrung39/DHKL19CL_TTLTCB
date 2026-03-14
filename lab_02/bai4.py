n = int(input("Nhap so nguyen: "))
if abs(n) >= 100:
    hang_tram = abs(n) // 100 % 10
    print("Chu so hang tram la: ", hang_tram)
else:
    print(0)