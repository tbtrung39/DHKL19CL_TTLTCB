str_a = input('Nhập chuỗi A: ')
str_b = input('Nhập chuỗi B: ')

tim_thay = False

if len(str_a) < 2 or len(str_b) < 2:
	print('Không tồn tại cách đặt!')
else:
	for i in range(1, len(str_a)):
		for j in range(1, len(str_b)):
			c = str_a[:i]
			d = str_a[i:]
			e = str_b[:j]
			f = str_b[j:]

			if int(c) + int(d) == int(e) + int(f):
				print(f'{c}+{d}={e}+{f}')
				tim_thay = True
				break

		if tim_thay:
			break

	if not tim_thay:
		print('Không tồn tại cách đặt!')
