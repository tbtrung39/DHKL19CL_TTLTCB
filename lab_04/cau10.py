n = input("Nhập số: ")
chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

if n[0] == '-':
    print("âm", end=" ")
    n = n[1:]

for ky_tu in n:
    so = int(ky_tu)
    print(chu[so], end=" ")