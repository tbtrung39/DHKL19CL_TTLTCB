while True:
    try:
        s = input("Nhập chuỗi: ")
        for kt in s:
            if not kt.isalpha() and kt != " ":
                raise Exception("Lỗi ký tự !!!")
        for i in range(len(s) - 3):
            if s[i] == s[i+1] == s[i+2] == s[i+3]:
                raise Exception("Lỗi nhập lặp lại !!!")
        for i in range(len(s) - 1):
            if s[i] == s[i+1] and s[i] != " ":
                raise Exception("Lỗi nhập liệu !!!")
        tu = s.split()
        for i in range(len(tu) - 4):
            if tu[i] == tu[i+1] == tu[i+2] == tu[i+3] == tu[i+4]:
                raise Exception("Lỗi nhập trùng lặp!!!")
        print("Chuỗi hợp lệ")
        break
    except Exception as e:
        print(e)