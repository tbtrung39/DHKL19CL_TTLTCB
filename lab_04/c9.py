s = input("Nhập chuỗi: ")

max_str = ""  
curr_str = ""     

i = 0

while i < len(s):
    if i == 0:
        curr_str = s[i]
    else:
        if s[i] == s[i - 1]:
            curr_str = curr_str + s[i]
        else:
            curr_str = s[i]

    if len(curr_str) > len(max_str):
        max_str = curr_str
    i = i + 1

print("Chuỗi con dài nhất:", max_str)