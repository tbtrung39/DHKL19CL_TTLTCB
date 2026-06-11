import my_Triage

a, b, c = 3, 4, 5
if my_Triage.is_TamGiac(a, b, c):
    print(f"Chu vi tam giac: {my_Triage.ChuViTamGiac(a, b, c)}")
    print(f"Dien tich tam giac: {my_Triage.S_TamGiac(a, b, c)}")
else:
    print("Ba canh khong tao thanh tam giac")