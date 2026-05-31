binary_dict = {}

for i in range(1, 101):
    binary_dict[i] = bin(i)[2:]
print("10 phần tử đầu tiên của từ điển nhị phân:")
for key in range(1, 11):
    print(f"{key}: '{binary_dict[key]}'")
