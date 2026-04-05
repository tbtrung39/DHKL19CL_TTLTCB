input_str = input('Nhập chuỗi Str: ')
split_str = input_str.split()
decimal_str = ''

for char in split_str:
    if char.isdecimal():
        decimal_str += char + ' '
print('Chuỗi sau khi xóa các ký tự không phải số:', decimal_str)

if decimal_str:
    for number in decimal_str.split():
        number = int(number)
        if number < 2:
            print(f'{number} không phải là số hoàn hảo.')
        else:
            total = 0

            for i in range(1, int(number) + 1):
                if number % i == 0:
                    total += 1
            if total == number:
                print(f'{number} là số hoàn hảo.')
            else:
                print(f'{number} không phải là số hoàn hảo.')
else:
    print('Không có số nào trong chuỗi.')
