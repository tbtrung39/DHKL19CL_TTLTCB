import random
n = int(input("Nhập số lượng phân tử: "))
A = set()
while len(A) < n :
    num = round(random.uniform(0.0, 100.0), 2)
    A.add(num)
print("Tập hợp A được sinh ra ngẫu nhiên:", A)
phan_tu_nho_nhat = min(A)
phan_tu_lon_nhat = max(A)
tong_cac_phan_tu = sum(A)
print(f"Phân tử nhỏ nhất là: {phan_tu_nho_nhat}")
print(f"Phân tử lớn nhất là: {phan_tu_lon_nhat}")
print(f"Tổng các phân tử:{tong_cac_phan_tu:.2f} ")