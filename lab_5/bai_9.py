s = input("Nhập chuỗi: ")
if not s:
    print("")
else:
    max_sub = current_sub = s[0]
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            current_sub += s[i]
        else:
            if len(current_sub) > len(max_sub):
                max_sub = current_sub
            current_sub = s[i]
    
    if len(current_sub) > len(max_sub):
        max_sub = current_sub
        
    print(f"Chuỗi con dài nhất gồm các ký tự giống nhau: {max_sub}")