def la_so_nguyen_to(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Nhập số tự nhiên n: "))
day_snt = []
s_hien_tai = 2
while len(day_snt) < n:
    if la_so_nguyen_to(s_hien_tai):
        day_snt.append(s_hien_tai)
    s_hien_tai += 1

print(f"{n} số nguyên tố đầu tiên là:", day_snt)