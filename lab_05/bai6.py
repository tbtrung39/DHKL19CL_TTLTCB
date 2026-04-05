s_input = input('Nhập chuỗi Str: ')
split_input = s_input.split()
hex_digits = "0123456789ABCDEFabcdef"
hex_str = ''

for char in s_input:
    if char in hex_digits:
        hex_str += char + ' '
print('Chuỗi sau khi lọc:', hex_str)

if hex_str:
    for char in hex_str.split():
        chuyen_hex = int(char, 16)
        print(f'Giá trị thập phân của ký tự hex {char} là: {chuyen_hex}')
else:
    print('Không có ký tự hex nào trong chuỗi.')