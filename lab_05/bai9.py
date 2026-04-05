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