import random
import math

def sinh_day_so():
    n = random.randint(1, 100) # Sinh ngau nhien so luong phan tu <= 100
    day_so = [random.randint(1, 1000) for _ in range(n)]
    print(f"Day so duoc sinh ra ({len(day_so)} phan tu): {day_so}")
    return day_so

def chia_het_cho_7(day_so):
    chia_7 = [x for x in day_so if x % 7 == 0]
    print(f"Cac so chia het cho 7: {chia_7}")

def tong_so_le(day_so):
    tong = sum([x for x in day_so if x % 2 != 0])
    print(f"Tong cac so le trong day: {tong}")

def kiem_tra_chinh_phuong(day_so):
    def la_so_cp(n):
        if n < 0: return False
        return math.isqrt(n)**2 == n
    
    chinh_phuong = [x for x in day_so if la_so_cp(x)]
    if chinh_phuong:
        print(f"Cac so chinh phuong trong day: {chinh_phuong}")
    else:
        print("Khong co so chinh phuong trong day.")