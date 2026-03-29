s = input("Nhập chuỗi: ")

so = ""
i = 0

while i < len(s):
    if '0' <= s[i] <= '9':
        so = so + s[i]
    i = i + 1

if so == "":
    print("Không có số trong chuỗi")
else:
    print("Chuỗi số sau khi lọc:", so)

    n = int(so)
    tong = 0
    i = 1
    while i < n:
        if n % i == 0:
            tong = tong + i
        i = i + 1
    if tong == n:
        print(n, "là số hoàn hảo")
    else:
        print(n, "không phải số hoàn hảo")