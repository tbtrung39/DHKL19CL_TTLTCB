with open("bai1\dayso.dat", "r") as f:
    numbers = list(map(int, f.read().split()))

tong = sum(x for x in numbers if x % 2 != 0)
print("Tổng các số hạng lẻ:", tong)