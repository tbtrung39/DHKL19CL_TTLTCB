with open(r"bai7/m_nums.txt", "r") as f:
    m_nums = set(map(int, f.read().split()))

with open(r"bai7/n_num.txt", "r") as f:
    n_nums = set(map(int, f.read().split()))

so_chung = sorted(m_nums & n_nums)

with open(r"bai7/so_chung.txt", "w") as f:
    f.write(" ".join(map(str, so_chung)))

with open(r"bai7/so_chung.txt", "r") as f:
    print(f.read())


