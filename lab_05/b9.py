s = input("Nhập chuỗi: ")

max_str = ""
current = s[0]

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        current += s[i]
    else:
        if len(current) > len(max_str):
            max_str = current
        current = s[i]

# kiểm tra lần cuối
if len(current) > len(max_str):
    max_str = current

print("Chuỗi con dài nhất:", max_str)