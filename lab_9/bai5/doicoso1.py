def nhap_so():
    return int(input("Nhập vào một số nguyên hệ 10: "))

def sang_nhi_phan(n):
    return bin(n)[2:]  

def sang_bat_phan(n):
    return oct(n)[2:]  

def sang_thap_luc_phan(n):
    return hex(n)[2:].upper() 