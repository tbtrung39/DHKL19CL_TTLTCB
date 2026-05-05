import math
R = input("Nhap ban kinh : ")
R = int(R)
def tinh_chuvi(R):
    cv = math.pi * 2 * R
    return cv
def tinh_dientich(R):
    S = math.pi * R**2
    return S
print(tinh_chuvi(R))
print(tinh_dientich(R))