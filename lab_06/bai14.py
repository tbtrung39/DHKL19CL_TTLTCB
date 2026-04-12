import re
s = input("Nhập các mật khẩu (cách nhau bởi dấu phẩy): ")
ds = s.split(",")
hop_le = []
for pw in ds:
    if (6 <= len(pw) <= 12 and
        re.search("[a-z]", pw) and
        re.search("[A-Z]", pw) and
        re.search("[0-9]", pw) and
        re.search("[$#@]", pw)):
        hop_le.append(pw)
print(",".join(hop_le))