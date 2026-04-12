while True:
    n = int(input("Nhập n nguyên dương: "))
    if n > 0: 
        break
    print("Vui lòng nhập lại!")
#Bài 8
s1 = sum(range(1, n + 1))
s2 = sum(range(1, 2*n + 2, 2))
s3 = sum(range(2, 2*n + 1, 2))
print(f"Kết quả Bài 8:")
print(f"a) S1 = {s1}")
print(f"b) S2 = {s2}")
print(f"c) S3 = {s3}")
print("-" * 30)
#Bài 9
s4 = 0
s5 = 0
s6 = 0
for i in range(1, n + 1):
    s4 += i**2
for i in range(1, 2*n + 2, 2):
    s5 += i**3
for i in range(2, 2*n + 1, 2):
    s6 += i**4

print(f"Kết quả Bài 9:")
print(f"a) S4 = {s4}")
print(f"b) S5 = {s5}")
print(f"c) S6 = {s6}")