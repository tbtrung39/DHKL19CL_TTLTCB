
ten = ["","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
while True:
    t = int(input("Nhap thu (1-7): "))
    if 1 <= t <= 7: 
        break
print(ten[t])