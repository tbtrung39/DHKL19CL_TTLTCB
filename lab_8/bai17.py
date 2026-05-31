from functools import reduce
n = int(input("Nhập số nguyên n: "))
danh_sach = list(range(1, n + 1))
so_chan = filter(lambda x: x % 2 == 0, danh_sach)
tong_so_chan = reduce(lambda x, y: x + y, so_chan, 0)

print(f"Tổng các số chẵn từ 1 đến {n} là: {tong_so_chan}")