m = input("Nhập các số tự nhiên: ")
Numbers = m.split()
Numbers = [int(x) for x in Numbers]
A = set(Numbers)
print("Tập hợp A:", A)
