n = input("Nhập một số nguyên: ")
tong = 0

for chu_so in n:
    if chu_so.isdigit():
        tong += int(chu_so)

print(f"Tổng các chữ số của {n} là: {tong}")