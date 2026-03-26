a = int(input("nhap so thu 1: "))
b = int(input("nhap so thu 2: "))

if a > b:
    lon = a
else:
    lon = b

while True:
    if lon % a == 0 and lon % b == 0:
        print(lon)
        break
    lon = lon + 1