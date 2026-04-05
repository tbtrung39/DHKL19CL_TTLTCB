binary_str = input('Nhập chuỗi nhị phân: ')

if binary_str == '':
	print('Chuỗi rỗng.')
else:
	hop_le = True
	decimal = 0

	for char in binary_str:
		if char != '0' and char != '1':
			hop_le = False
			break

	if hop_le:
		for char in binary_str:
			decimal = decimal * 2 + int(char)
		print('Số thập phân là:', decimal)
	else:
		print('Chuỗi không phải là số nhị phân hợp lệ.')
