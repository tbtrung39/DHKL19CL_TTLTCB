x = int(input("Nhập một số nguyên dương: "))
if x < 0:
    print("Vui lòng nhập một số nguyên dương.")
elif x < 10:
    print(f'Tổng của các chữ số của {x} là: {x}')
else:
    tong = 0
    while x > 0:
        chu_so = x % 10
        tong += chu_so
        x //= 10
    print(f'Tổng của các chữ số là: {tong}')
