def tim_max(n):
    if len(n) == 1:
        return n[0]

    flag = tim_max(n[1:])
    if flag > n[0]:
        return flag
    else:
        return n[0]

n = [int(x) for x in input("Nhập vào một dãy số: ").split()]
print(n)
print("Số lớn nhất trong dãy là:", tim_max(n))