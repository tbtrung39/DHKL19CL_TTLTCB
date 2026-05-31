W = input("Nhập vào chuỗi ký tự W: ")
sub_dict = {}
n = len(W)
for i in range(n):
    for j in range(i + 1, n + 1):
        sub_string = W[i:j]
        if sub_string in sub_dict:
            sub_dict[sub_string] += 1
        else:
            sub_dict[sub_string] = 1

print("Từ điển các chuỗi con và số lần xuất hiện:")
print(sub_dict)
