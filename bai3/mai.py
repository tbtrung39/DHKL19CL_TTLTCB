with open(r"bai3\f_in.dat", "r") as f:
    a = list(map(int, f.read().split()))

n = len(a)
cuc_tri = []

for k in range(1, n - 1):
    if (a[k-1] < a[k] > a[k+1]) or (a[k-1] > a[k] < a[k+1]):
        cuc_tri.append(a[k])

with open(r"bai3\f_out.dat", "w") as f:
    f.write(str(len(cuc_tri)) + "\n")
    f.write(" ".join(map(str, cuc_tri)))

print("Số lượng cực trị:", len(cuc_tri))
print("Các phần tử cực trị:", cuc_tri)