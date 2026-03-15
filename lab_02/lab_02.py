import math

def giai_bac_2(a, b, c):
    if a == 0:
        return f"x = {-c/b}" if b != 0 else ("Vô số nghiệm" if c == 0 else "Vô nghiệm")

    delta = b**2 - 4*a*c
    if delta < 0: return "Vô nghiệm"

    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    return f"x1 = {x1}, x2 = {x2}" if delta > 0 else f"Nghiệm kép x = {x1}"

def lay_hang_tram(n):
    return (abs(n) // 100) % 10

def doc_so(n):
    u = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    tr, ch, dv = n // 100, (n // 10) % 10, n % 10

    s = f"{u[tr]} trăm"
    s += " lẻ" if ch == 0 and dv != 0 else f" {u[ch]} mươi" if ch > 1 else " mười" if ch == 1 else ""

    if dv > 0:
        chu_dv = "mốt" if dv == 1 and ch > 1 else "lăm" if dv == 5 and ch > 0 else u[dv]
        s += f" {chu_dv}"
    return s.strip().capitalize()

def tinh_luong(tnct):
    he_so = 2.34 if tnct < 12 else 3.33 if tnct < 36 else 3.66 if tnct < 60 else 3.99
    return he_so * 1350000

def tinh_tien_san(bd, kt):
    h = kt - bd
    gia_goc = min(h, 3) * 100000 + max(0, h - 3) * 75000
    giam_gia = 0.9 if (bd >= 11 and kt <= 15) else 1.0
    return gia_goc * giam_gia

if __name__ == "__main__":
    print(f"Bài 2: {giai_bac_2(1, -3, 2)}")
    print(f"Bài 4: {lay_hang_tram(1234)}")
    print(f"Bài 6: {doc_so(515)}")
    print(f"Bài 8: {tinh_luong(40):,.0f} VNĐ")
    print(f"Bài 10: {tinh_tien_san(11, 14):,.0f} VNĐ")
