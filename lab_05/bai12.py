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