import random

def tao_day_ngau_nhien():
    so_luong = random.randint(10, 100)
    day_so = [random.randint(1, 1000) for _ in range(so_luong)]
    return day_so

def snt_chia_het_7(day_so):
    def kiem_tra_snt(n):
        if n < 2: return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0: return False
        return True
    return [x for x in day_so if kiem_tra_snt(x) and x % 7 == 0]

def tinh_tong_le(day_so):
    return sum([x for x in day_so if x % 2 != 0])

def kiem_tra_so_chinh_phuong(day_so):
    def is_scp(n):
        return int(n**0.5)**2 == n
    scp_list = [x for x in day_so if is_scp(x)]
    return scp_list if len(scp_list) > 0 else None