import math

a = float(input("Nhập vận tốc ban đầu a: "))

mau_so = math.log(5, 4)

t = (a**4) / mau_so

print(f"Thời gian để ô tô dừng hẳn là: {round(t, 2)} giây")
#