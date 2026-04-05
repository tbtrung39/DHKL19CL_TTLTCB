s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")
max_str = ""
for i in range(len(s1)):
    for j in range(i+1, len(s1)+1):
        sub = s1[i:j]
        if sub in s2 and len(sub) > len(max_str):
            max_str = sub
print("Chuỗi con chung dài nhất: ", max_str)