A = input("Nhập A: ")
B = input("Nhập B: ")
tim_thay = False
for i in range(1,len(A)):
    C = int(A[:i])
    D = int(A[i:])
    for j in range(1,len(B)):
        E = int(B[:j])
        F = int(B[j:])
        if C + D == E + F:
            print(f"{C} + {D} = {E} + {F}")
            tim_thay = True
    if not tim_thay:
        print("Không tồn tại cách đặt!")