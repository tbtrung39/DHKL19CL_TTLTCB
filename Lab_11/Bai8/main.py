from qlynhanvien import input_employees, compute_salary, print_table, save_csv


def main():
    emps = input_employees()
    compute_salary(emps)
    print('\nDanh sách nhân viên:')
    print_table(emps)
    emps_sorted = sorted(emps, key=lambda x: x['thuc_linh'], reverse=True)
    print('\nDanh sách theo thực lĩnh giảm dần:')
    print_table(emps_sorted)
    save_csv(emps_sorted)
    print('\nĐã lưu files/ds_nhanvien.csv')


if __name__ == '__main__':
    main()
