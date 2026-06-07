from modules import input_matrix, print_matrix, transpose, is_symmetric


def main():
    while True:
        try:
            n = int(input("Nhập kích thước N của ma trận vuông (N>0): "))
            if n <= 0:
                print("N phải lớn hơn 0. Thử lại.")
                continue
            break
        except ValueError:
            print("Vui lòng nhập số nguyên. Thử lại.")

    mat = input_matrix(n)
    print('\nMa trận vừa nhập:')
    print_matrix(mat)

    t = transpose(mat)
    print('\nMa trận chuyển vị:')
    print_matrix(t)

    if is_symmetric(mat):
        print('\nMa trận là ma trận đối xứng.')
    else:
        print('\nMa trận không đối xứng.')


if __name__ == '__main__':
    main()
