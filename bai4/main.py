def uoc_so_nguyen_to(n):
    uoc = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            uoc.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        uoc.append(n)
    return uoc

with open(r"bai4/f_in.dat", "r") as f:
    numbers = [int(line.strip()) for line in f if line.strip()]

with open(r"bai4/f_out.dat", "w") as f:
    for n in numbers:
        uoc = uoc_so_nguyen_to(n)
        f.write(" ".join(map(str, uoc)) + "\n")
        print(f"{n} -> {uoc}")

print('done')