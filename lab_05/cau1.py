nhap = input('nhap chuoi: ')
dem = 0
for i in nhap:
    if i.isdigit():
        dem = dem +1
print(dem)