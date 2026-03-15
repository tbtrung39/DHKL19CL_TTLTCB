xa, ya = map(float, input("Nhập tọa độ A (x y): ").split())
xb, yb = map(float, input("Nhập tọa độ B (x y): ").split())
xc, yc = map(float, input("Nhập tọa độ C (x y): ").split())
#
xg = (xa + xb + xc) / 3
yg = (ya + yb + yc) / 3

print(f"Tọa độ trọng tâm G là: ({round(xg, 2)}, {round(yg, 2)})")