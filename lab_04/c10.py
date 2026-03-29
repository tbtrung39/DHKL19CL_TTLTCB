s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")

max_str = ""
i = 0

while i < len(s1):
    j = 0
    while j < len(s2):
        k = 0
        temp = ""

        while (i + k < len(s1)) and (j + k < len(s2)) and (s1[i + k] == s2[j + k]):
            temp = temp + s1[i + k]
            k = k + 1

        if len(temp) > len(max_str):
            max_str = temp

        j = j + 1
    i = i + 1

print("Chuỗi con chung dài nhất:", max_str)