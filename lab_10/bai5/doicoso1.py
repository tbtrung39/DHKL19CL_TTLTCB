def nhap_so():
    return int(input("Nhap vao mot so nguyen duong: "))

def sang_nhi_phan(n):
    # bin(n) tra ve dang '0b1010', ta can bo '0b'
    print(f"He nhi phan: {bin(n)[2:]}")

def sang_bat_phan(n):
    # oct(n) tra ve dang '0o12', ta can bo '0o'
    print(f"He co so 8 (bat phan): {oct(n)[2:]}")

def sang_thap_luc_phan(n):
    # hex(n) tra ve dang '0xab', ta can bo '0x' va viet hoa .upper()
    print(f"He co so 16 (thap luc phan): {hex(n)[2:].upper()}")