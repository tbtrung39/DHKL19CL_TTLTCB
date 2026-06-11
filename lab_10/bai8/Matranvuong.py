def nhap_ma_tran():
    N = int(input("Nhap kich thuoc N cua ma tran vuong: "))
    ma_tran = []
    print(f"Nhap tung dong cua ma tran (moi so cach nhau khoang trang):")
    for i in range(N):
        while True:
            row = list(map(float, input(f"Dong {i+1}: ").split()))
            if len(row) == N:
                ma_tran.append(row)
                break
            print(f"Vui long nhap dung {N} phan tu.")
    return ma_tran, N

def in_ma_tran(ma_tran, N):
    print("Ma tran:")
    for row in ma_tran:
        print(" ".join([f"{x:g}" for x in row]))

def ma_tran_chuyen_vi(ma_tran, N):
    chuyen_vi = [[ma_tran[j][i] for j in range(N)] for i in range(N)]
    return chuyen_vi

def kiem_tra_doi_xung(ma_tran, N):
    for i in range(N):
        for j in range(i + 1, N):
            if ma_tran[i][j] != ma_tran[j][i]:
                return False
    return True