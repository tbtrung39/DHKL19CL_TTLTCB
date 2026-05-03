s = set()
print("Nhập ký tự (nhấn ESC để kết thúc): ")
while True:
    n = input("Nhập ký tự (dõ ESC để dừng): ")
    if n == "ESC":
        break
    s.add(n)
s2 = set()
for i in s:
    if not i.isdigit():
        s2.add(i)
print('Tập hợp sau khi xóa chữ số:',s2)