def input_students():
    n = int(input('Số sinh viên: '))
    students = []
    for i in range(n):
        print(f'-- SV {i+1} --')
        msv = input('Mã SV: ').strip()
        name = input('Họ tên: ').strip()
        tb = float(input('Điểm TB: '))
        rl = float(input('Điểm RL: '))
        students.append({'msv': msv, 'name': name, 'tb': tb, 'rl': rl})
    return students


def compute_tl(students):
    for s in students:
        s['tl'] = (s['tb'] + s['rl'])/2
    return students


def print_table(students):
    print(f"{'MSV':6} {'Họ tên':20} {'TB':6} {'RL':6} {'TL':6}")
    for s in students:
        print(f"{s['msv']:6} {s['name'][:20]:20} {s['tb']:6.2f} {s['rl']:6.2f} {s.get('tl',0):6.2f}")


def save_csv(students, path='files/ds_sinhvien.csv'):
    with open(path,'w', encoding='utf-8') as f:
        f.write('msv,name,tb,rl,tl\n')
        for s in students:
            f.write(f"{s['msv']},{s['name']},{s['tb']},{s['rl']},{s.get('tl',0)}\n")
