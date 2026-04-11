lst = [int(input(f"Nhập số {i+1}: ")) for i in range(int(input("Nhập n: ")))]
assert all(x % 2 == 0 for x in lst), "Có số lẻ trong list!"
print("Tất cả đều chẵn!")