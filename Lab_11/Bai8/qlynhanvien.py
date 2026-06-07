def input_employees():
    n = int(input('Số lượng nhân viên: '))
    emps = []
    for i in range(n):
        print(f'-- Nhân viên {i+1} --')
        manv = input('Mã NV: ').strip()
        ten = input('Họ tên: ').strip()
        chucvu = input('Chức vụ (TP/PP/NV): ').strip().upper()
        he_so = float(input('Hệ số lương: '))
        emps.append({'manv': manv, 'ten': ten, 'chucvu': chucvu, 'he_so': he_so})
    return emps


def compute_salary(emps):
    for e in emps:
        luong = e['he_so'] * 1490000
        if e['chucvu'] == 'TP':
            phucap = 1000000
        elif e['chucvu'] == 'PP':
            phucap = 700000
        else:
            phucap = 300000
        thuc_linh = luong + phucap
        e['luong'] = luong
        e['phucap'] = phucap
        e['thuc_linh'] = thuc_linh
    return emps


def print_table(emps):
    print(f"{'Mã':6} {'Họ tên':20} {'Cv':4} {'Hệ số':6} {'Lương':12} {'Phụ cấp':10} {'Thực lĩnh':12}")
    for e in emps:
        print(f"{e['manv']:6} {e['ten'][:20]:20} {e['chucvu']:4} {e['he_so']:6.2f} {e['luong']:12.0f} {e['phucap']:10.0f} {e['thuc_linh']:12.0f}")


def save_csv(emps, path='files/ds_nhanvien.csv'):
    with open(path,'w', encoding='utf-8') as f:
        f.write('manv,ten,chucvu,he_so,luong,phucap,thuc_linh\n')
        for e in emps:
            f.write(f"{e['manv']},{e['ten']},{e['chucvu']},{e['he_so']},{e['luong']},{e['phucap']},{e['thuc_linh']}\n")
