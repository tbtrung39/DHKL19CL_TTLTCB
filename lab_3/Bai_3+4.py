def la_so_nguyen_to(k):
    if k < 2: return False
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0: return False
    return True

n = int(input("Nhập n để kiểm tra nguyên tố: "))
# Bài 3
if la_so_nguyen_to(n):
    print(f"{n} là số nguyên tố.")
else:
    thap = n - 1
    cao = n + 1
    while True:
        if thap >= 2 and la_so_nguyen_to(thap):
            print(f"Số nguyên tố gần nhất là: {thap}")
            break
        if la_so_nguyen_to(cao):
            print(f"Số nguyên tố gần nhất là: {cao}")
            break
        thap -= 1
        cao += 1
# Bài 4        
print(f"Các số nguyên tố <= {n}:", [i for i in range(2, n + 1) if la_so_nguyen_to(i)])