import math

try:
    a = float(input("Nhap canh a: "))
    b = float(input("Nhap canh b: "))
    c = float(input("Nhap canh c: "))
    
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Lỗi: Chiều dài các cạnh phải là số dương lớn hơn 0!")
        
    if not (a + b > c and a + c > b and b + c > a):
        raise Exception("Lỗi: Ba số dương này không thỏa mãn điều kiện tồn tại tam giác!")
        
    p = (a + b + c) / 2
    dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"-> Diện tích tam giác là: {dien_tich:.2f}")

except ValueError as e:
    if "could not convert string to float" in str(e):
        print("Lỗi: Dữ liệu nhập vào không phải là kiểu số!")
    else:
        print(e)
except Exception as e:
    print(e)