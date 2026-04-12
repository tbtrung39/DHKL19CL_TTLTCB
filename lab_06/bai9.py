a = list(map(int, input("Nhập list: ").split()))
for x in a:
    assert x % 2 == 0, "Có số không chẵn"
print("Tất cả đều là số chẵn")