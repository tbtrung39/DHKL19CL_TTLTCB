nhap = input('nhap chuoi: ')
dem = 0 
for i in nhap:
    if not i.isalpha and not i.isdigit:
        dem= dem +1 
print(dem )