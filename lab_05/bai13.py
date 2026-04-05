A = input("Nhập A: ")
B = input("Nhập B: ")

tim = False

for i in range(1, len(A)):
    a1 = int(A[:i])
    a2 = int(A[i:])
    
    for j in range(1, len(B)):
        b1 = int(B[:j])
        b2 = int(B[j:])
        
        if a1 + a2 == b1 + b2:
            print(A[:i] + "+" + A[i:] + "=" + B[:j] + "+" + B[j:])
            tim = True
if not tim:
    print("Không tồn tại cách đặt")