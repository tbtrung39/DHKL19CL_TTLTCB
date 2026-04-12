n = int(input("Nhập n cho bài 6 & 7: "))
# Bài 6
tong_bac_3 = sum(i**3 for i in range(1, n + 1))
print(f"Tổng bậc 3 của {n} số đầu: {tong_bac_3}")

# Bài 7
tong_nghich_dao = sum(1/i for i in range(1, n + 1))
print(f"Tổng nghịch đảo: {round(tong_nghich_dao, 3)}")