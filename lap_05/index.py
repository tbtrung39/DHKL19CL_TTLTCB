def cau_1():
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

def cau_2():
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

def cau_3():
    Str1 = 'Khoa, Khoa học ứng dụng'
    tu = ''
    for char in Str1:
        if char != ' ' and char != ',':
            tu += char
        else:
            if tu != '':
                print(tu)
                tu = ''
    if tu != '':
        print(tu)

def cau_4():
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

def cau_5():
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

def cau_6():
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

def cau_7():
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

def cau_8():
    Str = """Python là một ngôn ngữ lập trình mạnh mẽ. \nLập trình Python rất thú vị và Python cũng rất dễ học.\nHọc lập trình không khó, chỉ cần chăm chỉ."""
    find_word = input('Nhập từ cần tìm: ').strip()
    split_words = Str.split()
    total_count = 0
    for word in split_words:
        if find_word in word:
            total_count += 1
    print(f'Từ "{find_word}" xuất hiện {total_count} lần trong chuỗi.')

def cau_9():
    s = input('Nhập chuỗi Str: ')
    if not s:
        print('Chuỗi rỗng.')
    else:
        ky_tu = ''
        tan_suat = []
        for char in s:
            if char not in ky_tu:
                ky_tu += char
                tan_suat.append(1)
            else:
                for i in range(len(ky_tu)):
                    if ky_tu[i] == char:
                        tan_suat[i] += 1
                        break
        max_index = 0
        for i in range(1, len(tan_suat)):
            if tan_suat[i] > tan_suat[max_index]:
                max_index = i
        ket_qua = ''
        for _ in range(tan_suat[max_index]):
            ket_qua += ky_tu[max_index]
        print('Chuỗi ký tự con có độ dài cực đại gồm các ký tự giống nhau:', ket_qua)

if __name__ == '__main__':
    cau_1()
    cau_2()
    cau_3()
    cau_4()
    cau_5()
    cau_6()
    cau_7()
    cau_8()
    cau_9()
