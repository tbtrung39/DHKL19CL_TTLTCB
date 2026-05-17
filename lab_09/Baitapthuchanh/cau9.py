def dao_nguoc(n):
    if n < 10:
        print(n, end="")
    else:
        print(n % 10, end="")
        dao_nguoc(n // 10)
n = input("Nhap n: ")
n = int(n)
dao_nguoc(n)
# Giải thích:
# vd nhập n = 123 -> dao_nguoc(123) -> print(3) -> dao_nguoc(12) -> print(2) -> dao_nguoc(1) -> print(1)
# -> return 321
# print(321)