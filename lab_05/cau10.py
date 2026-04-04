str1 = input("nhap chuoi 1: ")
str2 = input("nhap chuoi 2: ")

max_chuoi = ""

i = 0
while i < len(str1):
    j = 0
    while j < len(str2):
        k = 0
        while i+k < len(str1) and j+k < len(str2) and str1[i+k] == str2[j+k]:
            k += 1
        if k > len(max_chuoi):
            max_chuoi = str1[i:i+k]
        j += 1
    i += 1

print( max_chuoi)