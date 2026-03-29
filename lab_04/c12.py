chuoi = input("Nhập câu: ")

tu_hien_tai = ""
vi_tri = 0

while vi_tri < len(chuoi):
    ky_tu = chuoi[vi_tri]

    if ky_tu != " " and ky_tu != ",":
        tu_hien_tai = tu_hien_tai + ky_tu
    else:
        if tu_hien_tai != "":
            print(tu_hien_tai)
            tu_hien_tai = ""

    vi_tri = vi_tri + 1
#In
if tu_hien_tai != "":
    print(tu_hien_tai)