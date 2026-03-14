n = int(input("Nhập n: "))
if n < 0:
    n = -n
hang_tram = (n // 100) % 10

print("Chữ số hàng trăm:", hang_tram)