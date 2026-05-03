A = [161,182,161,154,176,170,167,171,170,174,150,142,148,165,170,178,156,145,149,163,
     162,159,165,165,170,180,155,159,155,153,152,162,180,168,169,168,167,170]
print("Số sinh viên trong nhóm: ",len(A))
tb = sum(A) / len(A)
B = set(A)
print("Các chiều cao khác nhau: ",B)
print("Chiều cao trung bình: ", round(tb,2))
