def main():
    with open('m_nums.txt','r') as f:
        a = f.read().strip().split()
    with open('n_nums.txt','r') as f:
        b = f.read().strip().split()
    set_a = set(int(x) for x in a)
    set_b = set(int(x) for x in b)
    common = sorted(list(set_a & set_b))
    with open('so_chung.txt','w') as f:
        if common:
            f.write(' '.join(str(x) for x in common))
    print('Số chung:', common)
    print('Đã ghi so_chung.txt')

if __name__ == '__main__':
    main()
