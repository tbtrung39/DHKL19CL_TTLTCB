str = input("Nhap chuoi: ")

so_str = ""
for char in str:
    if char.isdigit():
        so_str += char
print(f"chuoi so: {so_str}")

if so_str=="":
    print("Khong co so nao trong chuoi")
else:
    n=int(so_str)
    tong=0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    if tong == n:
        print(f"{n} la so hoan hao")
    else:
        print(f"{n} khong phai so hoan hao")
