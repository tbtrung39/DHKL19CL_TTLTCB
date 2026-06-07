def main():
    with open('matrix.txt','r') as f:
        lines = [line.rstrip('\n') for line in f]
    if not lines:
        print('File trống')
        return
    n = int(lines[0].strip())
    mat = []
    for i in range(1, 1+n):
        parts = lines[i].split()
        row = [int(x) for x in parts]
        mat.append(row)
    # a. Hiển thị nội dung dòng đầu và dòng thứ 3
    print('Dòng 1:', ' '.join(str(x) for x in mat[0]))
    if n >= 3:
        print('Dòng 3:', ' '.join(str(x) for x in mat[2]))
    # b. Hiển thị toàn bộ file
    print('\nToàn bộ ma trận:')
    for row in mat:
        print(' '.join(str(x) for x in row))
    # c. tìm các số lẻ và ghi vào ODD.txt ở dạng ma trận 4x4, vị trí không có số lẻ ghi 0
    odd_mat = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if mat[i][j] % 2 != 0:
                odd_mat[i][j] = mat[i][j]
    with open('ODD.txt','w') as f:
        for row in odd_mat:
            f.write(' '.join(str(x) for x in row) + '\n')
    # d. In ra nội dung dòng cuối cùng của ODD.txt
    with open('ODD.txt','r') as f:
        lines2 = f.read().strip().splitlines()
    if lines2:
        print('\nDòng cuối ODD.txt:')
        print(lines2[-1])
    else:
        print('\nODD.txt rỗng')

if __name__ == '__main__':
    main()
