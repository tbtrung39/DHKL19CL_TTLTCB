with open("bai2\Inp.txt", "r") as f:
    numbers = list(map(int, f.read().split()))

numbers.sort()

with open("bai2\out.dat", "w") as f:
    f.write(" ".join(map(str, numbers)))

print('done')