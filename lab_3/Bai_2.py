n = int(input("Nhap n de tim so hoan hao: "))
print(f"Cac so hoan hao nho hon {n}:", end="")
for i in range(1, n): 
    tong_uoc = sum(j for j in range(1, i) if i % j == 0 )
    if tong_uoc == i:
        print(i, end=" ")
print()





























