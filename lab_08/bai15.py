n = int(input("Nhập số phần tử: "))
a = []
for i in range(n):
    x = int(input("Nhập số: "))
    a.append(x)
chan = list(filter(lambda x: x % 2 == 0, a))
bp = list(map(lambda x: x ** 2, chan))
print("Các số chẵn: ", chan)
print("Bình phương số chẵn: ", bp)