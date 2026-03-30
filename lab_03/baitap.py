import math

# --- BÀI 9: TÍNH TỔNG S4, S5, S6 ---
def bai_9():
    print("\n--- BÀI 9 ---")
    while True:
        n = int(input("Nhập n (số nguyên dương): "))
        if n > 0:
            break
        print("n phải lớn hơn 0, vui lòng nhập lại!")
    
    s4 = sum(i**2 for i in range(1, n + 1))
    s5 = sum((2*i + 1)**3 for i in range(0, n)) # Tính n số hạng đầu: 1^3, 3^3...
    s6 = sum((2*i)**4 for i in range(1, n + 1))
    
    print(f"a) S4 = {s4}")
    print(f"b) S5 = {s5}")
    print(f"c) S6 = {s6}")

# --- BÀI 10: PHÂN TÍCH THỪA SỐ NGUYÊN TỐ ---
def bai_10():
    print("\n--- BÀI 10 ---")
    n = int(input("Nhập số nguyên dương cần phân tích: "))
    temp = n
    kq = []
    d = 2
    while temp > 1:
        while temp % d == 0:
            kq.append(str(d))
            temp //= d
        d += 1
    print(f"{n} = {' x '.join(kq)}")

# --- BÀI 11: VẼ TAM GIÁC SAO RỖNG (HÌNH B) ---
def bai_11():
    print("\n--- BÀI 11 (Vẽ hình b) ---")
    n = int(input("Nhập độ rộng (chiều cao) tam giác: "))
    for i in range(1, n + 1):
        for j in range(1, 2 * n):
            # In dấu * ở cạnh bên trái, cạnh bên phải hoặc đáy
            if j == n - i + 1 or j == n + i - 1 or i == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# --- BÀI 12: TÍNH SỐ KIỂM TRA CONTAINER ---
def bai_12():
    print("\n--- BÀI 12 ---")
    # Bảng tra cứu giá trị chữ cái (bỏ qua bội số của 11)
    mapping = {
        'A':10, 'B':12, 'C':13, 'D':14, 'E':15, 'F':16, 'G':17, 'H':18, 'I':19,
        'J':20, 'K':21, 'L':23, 'M':24, 'N':25, 'O':26, 'P':27, 'Q':28, 'R':29,
        'S':30, 'T':31, 'U':32, 'V':34, 'W':35, 'X':36, 'Y':37, 'Z':38
    }
    
    code = input("Nhập mã container (10 ký tự, VD: SUDU307007): ").upper()
    total_weight = 0
    
    for i in range(10):
        char = code[i]
        # Lấy giá trị tương ứng (nếu là số thì lấy chính nó, chữ thì tra bảng)
        val = int(char) if char.isdigit() else mapping[char]
        
        # Bước 1 & 2: Trọng số = giá trị * 2^i
        total_weight += val * (2**i)
    
    # Bước 3: Chia cho 11 lấy dư
    check_digit = total_weight % 11
    # Lưu ý: Nếu dư 10, số kiểm tra thường được quy ước là 0
    print(f"Tổng trọng số: {total_weight}")
    print(f"Số kiểm tra (Check digit): {check_digit % 10}")

# --- CHƯƠNG TRÌNH CHÍNH ---
if __name__ == "__main__":
    bai_9()
    bai_10()
    bai_11()
    bai_12()