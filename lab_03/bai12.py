container = input("Nhập mã container: ")

bang = {
    'A':10,'B':12,'C':13,'D':14,'E':15,'F':16,'G':17,'H':18,'I':19,
    'J':20,'K':21,'L':23,'M':24,'N':25,'O':26,'P':27,'Q':28,'R':29,
    'S':30,'T':31,'U':32,'V':34,'W':35,'X':36,'Y':37,'Z':38
}

tong = 0

for i in range(len(container)):
    ky_tu = container[i]

    if ky_tu.isdigit():
        gia_tri = int(ky_tu)
    else:
        gia_tri = bang[ky_tu]

    tong = tong + gia_tri * (2**i)

so_kiem_tra = tong % 11

print("Số kiểm tra:", so_kiem_tra)