s = input("Nhập chuỗi: ")
# Lấy các chữ số 
so = ""
for c in s:
    if c.isdigit():
        so += c
print("Chuỗi số: ", so)

# Kiểm tra số hoàn hảo
if so != "":
    n = int(so)
    tong = 0
    for i in range(1,n):
        if n % i == 0:
            tong += i
    if tong == n:
        print("Là số hoàn hảo")
    else:
        print("Không phải là số hoàn hảo")