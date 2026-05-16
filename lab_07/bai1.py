a = set()
while True:
    x = input("Nhập kí tự: ")
    if x == "ESC":
        break
    a.add(x)
print("Tập hợp:", a)
for i in list(a):
    if i.isdigit():
        a.remove(i)
print("Sau khi xoá số: ", a)
