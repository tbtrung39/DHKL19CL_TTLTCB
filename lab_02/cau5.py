months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
while True:
    thang = int(input("Nhập tháng (1-12): "))
    if 1 <= thang <= 12:
        break
    print("Tháng không hợp lệ, nhập lại!")
print("Tháng", thang, "là:", months[thang - 1])