a = [2,-4,1,9,-3,6,3,-2,6,8]

#1
sum = sum(a)
print(sum)

#2
so_hang_duong = 0
tong = 0
for so in a:
    if so > 0:
        so_hang_duong += 1
        tong = tong + so
print(so_hang_duong)
print(tong)

#3
serch_am_dau = -1
for i in range(len(a)):
    if a[i] <0:
        serch_am_dau = i
        break
print(serch_am_dau)

#4
serch_duong_cuoi = -1
for i in range(len(a)-1,-1,-1):
    if a[i] > 0:
        serch_duong_cuoi = i
        break
print(serch_duong_cuoi)

#5
max = [0]
vi_tri_max_cuoi = 0
for i in range(len(a)):
    if a[i]>max :
        max = a[i]
        vi_tri_max_cuoi = i
    elif a[i] == max:
        vi_tri_max_cuoi = i
print(max)
print(vi_tri_max_cuoi)
