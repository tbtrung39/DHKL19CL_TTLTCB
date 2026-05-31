def nhap_ma_tran():
    N = int(input("Nhập kích thước N của ma trận vuông (NxN): "))
    ma_tran = []
    for i in range(N):
        hang = [int(x) for x in input(f"Nhập {N} số cho hàng {i+1} (cách nhau khoảng trắng): ").split()]
        ma_tran.append(hang)
    return ma_tran, N

def in_ma_tran(ma_tran, N):
    for i in range(N):
        for j in range(N):
            print(f"{ma_tran[i][j]:<5}", end="")
        print()

def ma_tran_chuyen_vi(ma_tran, N):
    chuyen_vi = [[ma_tran[j][i] for j in range(N)] for i in range(N)]
    return chuyen_vi

def kiem_tra_doi_xung(ma_tran, N):
    for i in range(N):
        for j in range(i, N):
            if ma_tran[i][j] != ma_tran[j][i]:
                return False
    return True