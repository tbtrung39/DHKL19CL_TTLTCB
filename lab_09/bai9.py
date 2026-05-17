def dao_nguoc_so(so, ket_qua=0):
    if so == 0:
        return ket_qua
    return dao_nguoc_so(so // 10, ket_qua * 10 + so % 10)

n = int(input())
print(dao_nguoc_so(n))