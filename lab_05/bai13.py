A = input("Nhập A: ")
B = input("Nhập B: ")
tim_duoc = False
# Chia A
for i in range(1, len(A)):
    C = int(A[:i])
    D = int(A[:i])
# Chia B
    for j in range(1, len(B)):
        E = int(B[:j])
        F = int(B[i:])
        if C + D == E + F:
            print(f"{C}+{D}={E}+{F}")
            tim_duoc = True
            break
    if tim_duoc:
        break
if not tim_duoc:
    print("Không tồn tại cách đặt")
