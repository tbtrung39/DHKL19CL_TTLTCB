n = []

while True:
    x = int(input("Nhap so nguyen (nhap q de thoat): "))
    if x == 'q':
        break
    n.append(x)

# tim phan tu lon thu 2 va vi tri cua no
if len(n) < 2:
    print("Khong co phan tu lon thu 2 trong mang.")
else:
    max_value = n[0]
    second_max_value = 0
    max_index = 0
    second_max_index = 0
    for i in range(1, len(n)):
        if n[i] > max_value:
            second_max_value = max_value
            second_max_index = max_index
            max_value = n[i]
            max_index = i
        elif n[i] > second_max_value and n[i] != max_value:
            second_max_value = n[i]
            second_max_index = i
    if second_max_value == 0:
        print("Khong co phan tu lon thu 2 trong mang.")
    else:
        print("Phan tu lon thu 2 trong mang la: ", second_max_value)
        print("Vi tri cua phan tu lon thu 2 trong mang la: ", second_max_index)

# so luong cac so nguyen duong lien tiep trong a
max_count = 0
current_count = 0
for i in range(len(n)):
    if n[i] > 0:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 0
print("So luong cac so nguyen duong lien tiep trong mang la: ", max_count)

#so luong cac so duong lien tiep co tong lon nhat trong a
max_sum = 0
current_sum = 0
current_count = 0
for i in range(len(n)):
    if n[i] > 0:
        current_sum += n[i]
        current_count += 1
        if current_sum > max_sum:
            max_sum = current_sum
            max_count = current_count
    else:
        current_sum = 0
        current_count = 0
print("So luong cac so duong lien tiep co tong lon nhat trong mang la: ", max_count)
