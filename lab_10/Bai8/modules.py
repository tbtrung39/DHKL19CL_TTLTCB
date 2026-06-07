def input_matrix(n):
    mat = []
    print(f"Nhập ma trận {n}x{n}, mỗi dòng nhập {n} số, cách nhau bằng khoảng trắng:")
    for i in range(n):
        while True:
            line = input(f"Dòng {i+1}: ").strip()
            parts = line.split()
            if len(parts) != n:
                print(f"Vui lòng nhập đúng {n} số trong một dòng.")
                continue
            try:
                row = [int(x) for x in parts]
            except ValueError:
                print("Chỉ nhập số nguyên. Thử lại.")
                continue
            mat.append(row)
            break
    return mat


def print_matrix(mat):
    for row in mat:
        print(' '.join(str(x) for x in row))


def transpose(mat):
    n = len(mat)
    t = [[mat[j][i] for j in range(n)] for i in range(n)]
    return t


def is_symmetric(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i+1, n):
            if mat[i][j] != mat[j][i]:
                return False
    return True
