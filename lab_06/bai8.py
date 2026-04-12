#voi n duoc nhap tu ban phim. Hay viet chuong trinh su dung list comprehension de in day Fibonacci duoi dang tach biet dang dau ","
n = int(input("Nhap so n: "))
fibonacci = [0, 1]
for i in range(2, n):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
print("Day Fibonacci: ", ", ".join(str(x) for x in fibonacci[:n]))

