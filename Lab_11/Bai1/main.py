def read_numbers(path):
    nums = []
    with open(path, 'r') as f:
        for line in f:
            parts = line.split()
            for p in parts:
                try:
                    nums.append(int(p))
                except:
                    pass
    return nums


def main():
    nums = read_numbers('dayso.dat')
    s = 0
    # tính tổng các số hạng ở vị trí lẻ (1-based)
    for i, v in enumerate(nums, start=1):
        if i % 2 == 1:
            s += v
    print('Tổng các số hạng ở vị trí lẻ:', s)


if __name__ == '__main__':
    main()
