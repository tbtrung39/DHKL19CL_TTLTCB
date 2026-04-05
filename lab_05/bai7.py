Str = input("Nhập chuỗi: ")
chuoi_so = ""
for i in Str:
    if i.isdigit():
        chuoi_so = chuoi_so + i
print("Chuỗi số:", chuoi_so)
if chuoi_so == "":
    print("Không có số để kiểm tra.")
else:
    n = int(chuoi_so)
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong = tong + i
    if tong == n:
        print(n, "là số hoàn hảo.")
    else:
        print(n, "không phải là số hoàn hảo.")