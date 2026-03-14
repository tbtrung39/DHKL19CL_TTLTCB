n = input("Nhập số nguyên: ")
num = int(n)
if num >= 100 or num <= -100:
    hang_trăm = abs(num) // 100 % 10
    print("Chữ số hàng trăm là:", hang_trăm)
else:
    print("0")
