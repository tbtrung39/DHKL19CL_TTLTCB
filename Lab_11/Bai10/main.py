from My_QuanLySinhvien import quanlysinhvien as qlv


def main():
    students = qlv.input_students()
    qlv.compute_tl(students)
    print('\nDanh sách sinh viên:')
    qlv.print_table(students)
    students_sorted = sorted(students, key=lambda x: x['rl'])
    print('\nDanh sách theo RL tăng dần:')
    qlv.print_table(students_sorted)
    # student(s) with highest TL
    max_tl = max(s['tl'] for s in students)
    best = [s for s in students if s['tl'] == max_tl]
    print('\nSinh viên có điểm TL cao nhất:')
    qlv.print_table(best)
    # save
    import os
    if not os.path.isdir('files'):
        os.mkdir('files')
    qlv.save_csv(students, path='files/ds_sinhvien.csv')
    print('\nĐã lưu files/ds_sinhvien.csv')


if __name__ == '__main__':
    main()
