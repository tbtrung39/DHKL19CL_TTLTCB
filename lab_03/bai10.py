n = input("Nhập n: ")
n = int(n)
print("Phân tích", n, "thành các thừa số nguyên tố: ", end="")
i = 2
while n > 1:
    if n % i == 0:
        print(i,end=" ")
        n = n // i
    else:
        i = i + 1
