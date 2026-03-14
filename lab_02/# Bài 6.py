# Bài 6:
n = input("Nhập số nguyên có 3 chữ số: ")
num = int(n)
tram = num // 100
chuc = (num % 100) // 10
don_vi = num % 10
print(f"{tram} trăm {chuc} chục {don_vi} đơn vị")