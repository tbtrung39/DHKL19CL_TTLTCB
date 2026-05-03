A = {1,2,3.5,7.2,"hello","python",10,4.8,"abc"}
dem_songuyen = 0
dem_sothuc = 0
dem_chuoi = 0
for i in A:
    if type(i) == int:
        dem_songuyen = dem_songuyen + 1
    elif type(i) == float:
        dem_sothuc = dem_sothuc + 1
    elif type(i) == str:
        dem_chuoi = dem_chuoi + 1
print("Tập hợp A:",A)
print("Số phần tử là số nguyên:",dem_songuyen)
print("Số phần tử là số thực:",dem_sothuc)
print("Số phần tử là chuỗi:",dem_chuoi)