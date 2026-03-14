s = int(input("Nhap so giay: "))
d = s // 86400
s = s % 86400
h = s // 3600
s = s % 3600
m = s // 60
s = s % 60
print(f"Ket qua: {d} ngay, {h} gio, {m} phut, {s} giay") 