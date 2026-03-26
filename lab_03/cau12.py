container = input("Nhap 10 ky tu container (4 chu cai + 6 so): ").upper()

while len(container) != 10:
    container = input("Nhap lai 10 ky tu: ").upper()

tong = 0
for i in range(4):
    c = container[i]
    if c == 'A': gt = 10
    elif c == 'B': gt = 12
    elif c == 'C': gt = 13
    elif c == 'D': gt = 14
    elif c == 'E': gt = 15
    elif c == 'F': gt = 16
    elif c == 'G': gt = 17
    elif c == 'H': gt = 18
    elif c == 'I': gt = 19
    elif c == 'J': gt = 20
    elif c == 'K': gt = 21
    elif c == 'L': gt = 23
    elif c == 'M': gt = 24
    elif c == 'N': gt = 25
    elif c == 'O': gt = 26
    elif c == 'P': gt = 27
    elif c == 'Q': gt = 28
    elif c == 'R': gt = 29
    elif c == 'S': gt = 30
    elif c == 'T': gt = 31
    elif c == 'U': gt = 32
    elif c == 'V': gt = 34
    elif c == 'W': gt = 35
    elif c == 'X': gt = 36
    elif c == 'Y': gt = 37
    elif c == 'Z': gt = 38
    else: gt = 0
    
    tong = tong + gt * (2 ** i)

for i in range(4, 10):
    so = ord(container[i]) - 48  # '0' là 48
    tong = tong + so * (2 ** i)

check_digit = tong % 11
if check_digit == 10:
    check_digit = 0

print("So kiem tra:", check_digit)