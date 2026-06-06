# Bài 5:
# Hàm đệ quy tính S1
def tinh_s1(n):
    if n == 1:
        return 1
    return n + tinh_s1(n - 1)

# Hàm đệ quy tính S2
def tinh_s2(n):
    if n == 1:
        return 1
    return (n**2) + tinh_s2(n - 1)

def main():
    try:
        # Nhập dữ liệu
        n_input = input("Nhập số nguyên dương n: ")
        
        # Kiểm tra dữ liệu nhập vào (n phải là số nguyên)
        if not n_input.isdigit():
            raise ValueError("Lỗi: Bạn phải nhập vào một số nguyên!")
        
        n = int(n_input)
        
        # Kiểm tra n >= 1
        if n < 1:
            raise ValueError("Lỗi: n phải lớn hơn hoặc bằng 1!")
        
        # Tính toán và in kết quả
        print(f"Tổng S1 = 1 + 2 + ... + {n} = {tinh_s1(n)}")
        print(f"Tổng S2 = 1^2 + 2^2 + ... + {n}^2 = {tinh_s2(n)}")
        
    except ValueError as e:
        print(e)
    except RecursionError:
        print("Lỗi: n quá lớn, vượt quá giới hạn đệ quy của hệ thống!")

if __name__ == "__main__":
    main()