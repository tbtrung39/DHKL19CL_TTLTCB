C_plus_plus = {"sv01", "sv02", "sv03", "sv05"}
Java = {"sv02", "sv04", "sv05", "sv06"}
Python = {"sv05", "sv06", "sv07"}
thi_3_mon = C_plus_plus & Java & Python
thi_it_nhat_2_mon = (C_plus_plus & Java) | (Java & Python) | (C_plus_plus & Python)
thi_2_mon = thi_it_nhat_2_mon - thi_3_mon
tat_ca_sv = C_plus_plus | Java | Python
thi_1_mon = tat_ca_sv - thi_it_nhat_2_mon

print("Sinh viên thi cả 3 môn:", thi_3_mon)
print("Sinh viên thi đúng 2 môn:", thi_2_mon)
print("Sinh viên chỉ thi 1 môn:", thi_1_mon)
