import sohoc
import phuongtrinh

# Test so hoc
print(f"UCLN(12, 18) = {sohoc.Ucln(12, 18)}")
print(f"Tong cac uoc cua 6 = {sohoc.SumDivisor(6)}")

# Test phuong trinh
print("Giai phuong trinh bac 2 (1x^2 - 3x + 2 = 0):")
print(phuongtrinh.giai_bac_hai(1, -3, 2))