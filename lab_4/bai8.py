bang_ascii = {
    'A': 65, 'B': 66, 'C': 67,
    'a': 97, 'b': 98, 'c': 99,
    '0': 48, '1': 49, '2': 50
}
asciis = input("Nhập ký tự: ")

i = 0
while i < len(asciis):
    if asciis[i] in bang_ascii:
        print("ASCII =", bang_ascii[asciis[i]])
    else:
        print("Không có trong bảng")
    i += 1