'''
Nhập vào 1 số nguyên yêu cầu xuất ra chữ số hàng trăm của số đó
Nếu không có thì xuất ra 0.
'''
n = int(input("Nhập số nguyên: "))
if n >= 100:
    a = n // 100
    a = a % 10
    print("Chữ số hàng phần trăm là: ", a)
else:
    print("Nhập lại: ")