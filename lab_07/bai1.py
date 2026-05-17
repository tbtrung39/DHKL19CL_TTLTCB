n = input("Nhập các kí tự (nhập 'exit' để kết thúc): ")
s = set()
while n != "exit":
    s.add(n)
    n = input("Nhập các kí tự (nhập 'exit' để kết thúc): ")
for i in list(s):
    if i.isdigit():
        s.remove(i)
print("Set sau khi xóa các phần tử là kí tự số:", s)