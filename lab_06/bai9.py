a = list(map(int, input("Nhập list: ").split()))
for i in a: 
    assert i % 2 == 0, " Có phần tử không phải số chẵn" 
print("Tất cả các phần tử trong list đều là số chẵn.")