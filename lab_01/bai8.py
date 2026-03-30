x, y, z = map(float, input("Nhập tọa độ điểm M (x y z): ").split())
#
print(f"Đối xứng qua Oxy: ({x}, {y}, {-z})")
print(f"Đối xứng qua Oxz: ({x}, {-y}, {z})")
print(f"Đối xứng qua Oyz: ({-x}, {y}, {z})")