#1
s = input("Nhập chuỗi: ")
count = 0
for char in s:
    if '0' <= char <= '9': # Kiểm tra xem ký tự có nằm trong khoảng từ 0-9
        count += 1
print(f"Số lượng ký tự là số: {count}")

#2
s = input("2. Nhập chuỗi: ")
count = 0
for char in s:
    is_alnum = ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')
    if not is_alnum:
        count += 1
print("Số ký tự đặc biệt/tiếng Việt:", count)

#3
n = int(input("3. Nhập số n: "))
if n == 0:
    res = "0"
else:
    res = ""
    temp = n
    while temp > 0:
        res = str(temp % 2) + res
        temp //= 2
print(f"Số {n} sang nhị phân là: {res}")

#4
s1 = input("4. Nhập Str1: ")
s2 = input("4. Nhập Str2: ")
res = ""
i = 0
while i < len(s1) and i < len(s2):
    res += s1[i] + s2[i]
    i += 1
res += s1[i:] + s2[i:] # Cộng phần còn lại của chuỗi dài hơn
print("Kết quả trộn:", res)

#5
s = input("5. Nhập chuỗi: ")
num_str = ""
for char in s:
    if '0' <= char <= '9':
        num_str += char

if num_str:
    n = int(num_str)
    print("Số lọc được:", n)
    tong = 0
    for i in range(1, n):
        if n % i == 0: tong += i
    if tong == n and n != 0:
        print(f"{n} là số hoàn hảo")
    else:
        print(f"{n} không phải số hoàn hảo")
else:
    print("Không có số trong chuỗi")

#6
s = input("6. Nhập chuỗi Hex: ").upper()
hex_chars = "0123456789ABCDEF"
is_hex = True
clean_s = ""

for char in s:
    if char in hex_chars:
        clean_s += char
    else:
        is_hex = False

if is_hex:
    print(f"Chuỗi {s} hợp lệ. Thập phân: {int(s, 16)}")
else:
    print(f"Không hợp lệ. Đã loại bỏ ký tự lạ: {clean_s}")
    if clean_s: print(f"Chuyển phần còn lại sang thập phân: {int(clean_s, 16)}")

#7
s = input("5. Nhập chuỗi: ")
num_str = ""
for char in s:
    if '0' <= char <= '9':
        num_str += char

if num_str:
    n = int(num_str)
    print("Số lọc được:", n)
    tong = 0
    for i in range(1, n):
        if n % i == 0: tong += i
    if tong == n and n != 0:
        print(f"{n} là số hoàn hảo")
    else:
        print(f"{n} không phải số hoàn hảo")
else:
    print("Không có số trong chuỗi")

#8
s = input("8. Nhập đoạn văn: ")
word_to_find = input("Nhập từ cần tìm: ")
words = s.split() # Tách theo khoảng trắng
count = 0
for w in words:
    if w.strip(".,!?;:") == word_to_find: # Loại bỏ dấu câu quanh từ
        count += 1
print(f"Tìm thấy '{word_to_find}' {count} lần")

#9
s = input("9. Nhập chuỗi: ")
if not s: print("")
else:
    max_sub = current_sub = s[0]
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            current_sub += s[i]
        else:
            if len(current_sub) > len(max_sub): max_sub = current_sub
            current_sub = s[i]
    if len(current_sub) > len(max_sub): max_sub = current_sub
    print("Kết quả:", max_sub)

#10
s1 = input("10. Nhập Str1: ")
s2 = input("10. Nhập Str2: ")
res = ""
for i in range(len(s1)):
    for j in range(i + 1, len(s1) + 1):
        sub = s1[i:j]
        if sub in s2 and len(sub) > len(res):
            res = sub
print("Chuỗi con chung dài nhất:", res)

#11
b = input("11. Nhập chuỗi nhị phân: ")
tp = 0
for i in range(len(b)):
    bit = int(b[-(i+1)]) # Lấy từ phải sang trái
    tp += bit * (2 ** i)
print("Giá trị thập phân:", tp)

#12
s = input("12. Nhập chuỗi: ")
temp = ""
for char in s:
    if char == ' ' or char == ',':
        if temp: 
            print(temp)
            temp = ""
    else:
        temp += char
if temp: print(temp)

#13
A = input("13. Nhập chuỗi A: ")
B = input("13. Nhập chuỗi B: ")
found = False

for i in range(1, len(A)):
    C = int(A[:i])
    D = int(A[i:])
    for j in range(1, len(B)):
        E = int(B[:j])
        F = int(B[j:])
        if C + D == E + F:
            print(f"Đẳng thức đúng: {C}+{D}={E}+{F}")
            found = True
            break
    if found: break

if not found:
    print("Không tồn tại cách đặt!")
    