chuoi = input("Nhập các mật khẩu (cách nhau bởi dấu phẩy): ")

danh_sach = [p.strip() for p in chuoi.split(",")]

hop_le = [p for p in danh_sach if
          any(c.islower() for c in p) and
          any(c.isdigit() for c in p) and
          any(c.isupper() for c in p) and
          any(c in "$#@" for c in p) and
          6 <= len(p) <= 12]

print("Mật khẩu hợp lệ:", ",".join(hop_le)) 