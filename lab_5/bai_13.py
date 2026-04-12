A = input("Nhập chuỗi A: ")
B = input("Nhập chuỗi B: ")

found = False
for i in range(len(A) + 1):
    if i == 0 or i == len(A):
        val_a = int(A)
        expr_a = A
    else:
        val_a = int(A[:i]) + int(A[i:])
        expr_a = A[:i] + "+" + A[i:]
    for j in range(len(B) + 1):
        if j == 0 or j == len(B):
            val_b = int(B)
            expr_b = B
        else:
            val_b = int(B[:j]) + int(B[j:])
            expr_b = B[:j] + "+" + B[j:]
        if val_a == val_b:
            print(f"Đẳng thức đúng: {expr_a}={expr_b}")
            found = True
            break 
            
    if found: 
        break 

if not found:
    print("Không tồn tại cách đặt!")