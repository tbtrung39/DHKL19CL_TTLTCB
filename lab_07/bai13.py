W = input("Nhập một chuỗi kí tự: ")
dictionary = {}
for i in range(len(W)):
    for j in range(i + 1, len(W) + 1):
        K = W[i:j]
        if K in dictionary:
            dictionary[K] += 1
        else:
            dictionary[K] = 1
print("Từ điển chứa các cặp (K, V):", dictionary)