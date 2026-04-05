str1 = input('Nhập chuỗi Str1: ')
str2 = input('Nhập chuỗi Str2: ')

max_len = 0
max_sub = ''

for i in range(len(str1)):
	for j in range(len(str2)):
		k = 0
		while i + k < len(str1) and j + k < len(str2) and str1[i + k] == str2[j + k]:
			k += 1

		if k > max_len:
			max_len = k
			max_sub = str1[i:i + k]

if max_len > 0:
	print('Chuỗi con chung dài nhất là:', max_sub)
	print('Độ dài:', max_len)
else:
	print('Không có chuỗi con chung giữa Str1 và Str2.')
