a = [2, 4, 6, 8] # Danh sách nhập vào
for x in a:
    assert x % 2 == 0, f"{x} không chẵn"
print("Tất cả đều chẵn")