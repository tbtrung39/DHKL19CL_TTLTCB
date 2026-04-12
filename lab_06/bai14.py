chuoi_nhap = "ABd1234@1, a F1#,2w3E*, 2We3345"
danh_sach_mk = chuoi_nhap.split(',')

chuoi_ket_qua = ""

for mk in danh_sach_mk:
    mk = mk.strip() 
    
    if len(mk) < 6 or len(mk) > 12:
        continue 
        
    co_chu_thuong = False
    co_chu_hoa = False
    co_so = False
    co_ky_tu_dac_biet = False
    
    for ky_tu in mk:
        if 'a' <= ky_tu <= 'z':
            co_chu_thuong = True
        elif 'A' <= ky_tu <= 'Z':
            co_chu_hoa = True
        elif '0' <= ky_tu <= '9':
            co_so = True
        elif ky_tu in "$#@":
            co_ky_tu_dac_biet = True
            
    if co_chu_thuong and co_chu_hoa and co_so and co_ky_tu_dac_biet:
        if chuoi_ket_qua == "":
            chuoi_ket_qua = mk
        else:
            chuoi_ket_qua = chuoi_ket_qua + "," + mk

print("Đầu ra:", chuoi_ket_qua) 
