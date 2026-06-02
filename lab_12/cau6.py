ds_email = []
while True:
    try:
        username = input("Nhập username: ")
        if username.lower() == "stop":
            break
        if " " in username:
            raise Exception("Loi: username khong duoc chua dau cach!")
        if not username.isalnum():
            raise Exception("Loi: username chi gom chu va so!")
        email = username + "@companyname.com"
        ds_email.append(email)
        print("email da tao: ", email)
    except Exception as e:
        print(e)
print("Danh sach email:")
for x in ds_email:
    print(x)