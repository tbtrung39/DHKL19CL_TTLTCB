n = int(input("Nhập một số nguyên n: "))
dictionary = {i: i * i for i in range(1, n + 1)}
print("Dictionary chứa (i, i*i):", dictionary)