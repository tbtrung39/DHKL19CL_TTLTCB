# a. Nhập từ bàn phím số tự nhiên:
n = int(input("Nhập một số tự nhiên: "))
# b. In ra màn hình dãy n số nguyên tố đầu tiên:
NguyenTo = []
for i in range(2, n * 10):  
    if all(i % j != 0 for j in range(2, int(i**0.5) + 1)):
        NguyenTo.append(i)
    if len(NguyenTo) == n:
        break
print(f"{n} số nguyên tố đầu tiên:", NguyenTo)