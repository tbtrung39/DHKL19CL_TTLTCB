def tinh_S1(n):
    if n == 1:
        return 1
    return n + tinh_S1(n - 1)

def tinh_S2(n):
    if n == 1:
        return 1
    return n**2 + tinh_S2(n - 1)

try:
    nhap_n = input("Nhap vao so nguyen duong n: ")
    
    if not nhap_n.isdigit():
        raise ValueError("Lỗi: Giá trị n nhập vào không hợp lệ (Phải là số nguyên)!")
        
    n = int(nhap_n)
    
    if n < 1:
        raise ValueError("Lỗi: n phải là số nguyên dương lớn hơn hoặc bằng 1!")
        
    print(f"-> Kết quả S1 = {tinh_S1(n)}")
    print(f"-> Kết quả S2 = {tinh_S2(n)}")

except ValueError as e:
    print(e)
except RecursionError:
    print("Lỗi: Số n quá lớn gây ra hiện tượng tràn tầng đệ quy!")