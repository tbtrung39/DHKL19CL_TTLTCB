str = input("Nhập chuỗi: ")

max_chuoi = ""
i = 0

while i < len(str):
    j = i
    while j < len(str) and str[j] == str[i]:
        j += 1
    if j - i > len(max_chuoi):
        max_chuoi = str[i] * (j - i)
    i = j

print( max_chuoi)