import re
passwords = input("Nhập mật khẩu: ").split(',')
hop_le = []
for p in passwords:
    if (6 <= len(p) <= 12 and
        re.search("[a-z]", p) and
        re.search("[A-Z]", p) and
        re.search("[0-9]", p) and
        re.search("[$#@]", p)):
        hop_le.append(p)
print(",".join(hop_le))