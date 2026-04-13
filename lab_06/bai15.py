ds = []
while True:
    s = input("Nhập (name,age,score) hoặc Enter để dừng: ")
    if s == "":
        break
    name, age, score = s.split(',')
    ds.append((name, int(age), int(score)))
ds.sort(key=lambda x: (x[0], x[1], x[2]))
print(ds)