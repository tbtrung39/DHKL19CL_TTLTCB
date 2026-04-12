a = []
while True:
    n = int(input("Nhập số (0 để dừng): "))
    if n == 0: break
    a.append(n)

duong = [x for x in a if x > 0]
con_lai = [x for x in a if x <= 0]
a = duong + con_lai
print("Danh sách sau khi đưa số dương lên đầu:", a)

m = int(input("Nhập số m cần chèn: "))
a.insert(0, m)          
a.append(m)              
if len(a) >= 5:
    a.insert(4, m)       
print("Danh sách sau khi chèn m:", a)