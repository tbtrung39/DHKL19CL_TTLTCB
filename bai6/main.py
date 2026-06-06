with open("bai6/data.txt", "w") as f:
    f.write("4\n")
    f.write("211 133 180 5\n")
    f.write("192 168 1 254\n")
    f.write("11 1 11 233\n")

with open("bai6/data.txt", "r") as f:
    lines = f.readlines()

print("Dòng 1:", lines[0].strip())
print("Dòng 3:", lines[2].strip())

for line in lines:
    print(line.strip())

matrix = []
for line in lines:
    row = []
    for x in line.split():
        if x.lstrip('-').isdigit():
            num = int(x)
            row.append(num if num % 2 != 0 else 0)
    if row:
        matrix.append(row)

with open("bai6/ODD.txt", "w") as f:
    for row in matrix:
        line_out = " ".join(map(str, row))
        f.write(line_out + "\n")
        print(line_out)

with open("bai6/ODD.txt", "r") as f:
    odd_lines = f.readlines()
print(odd_lines[-1].strip())