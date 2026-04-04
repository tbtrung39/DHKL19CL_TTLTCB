A = input("Nhập chuỗi A: ")
B = input("Nhập chuỗi B: ")

tim_thay = False

for i in range(1, len(A)):
    for j in range(1, len(B)):
        C = int(A[:i]) + int(A[i:])
        D = int(B[:j]) + int(B[j:])
        if C == D:
            print(f"{A[:i]}+{A[i:]}={B[:j]}+{B[j:]}")
            tim_thay = True

if not tim_thay:
    print("Không tồn tại cách đặt!")