n = int(input('nhap so phan tu: '))
list = []
for i in range(n):
    x = int(input(f'nhap phan tu thu {i+1}: '))
    list.append(x)

#1
sx_max = sorted(set(list), reverse=True)
max2 = sx_max[1]
vi_tri_max2 = list.index(max2)
print(max2)
print(vi_tri_max2)

#2
max_count = 0
count = 0
for i in list:
    if i>0:
        count = count+1
        max_count = max(max_count, count)
    else:
        count = 0
print(max_count)

#3
max_sum = cur_sum = 0
best_len = cur_len = 0
for x in list:
    if x > 0:
        cur_sum += x
        cur_len += 1
    else:
        if cur_sum > max_sum:
            max_sum, best_len = cur_sum, cur_len
        cur_sum = cur_len = 0
if cur_sum > max_sum:
    best_len = cur_len
print(best_len)