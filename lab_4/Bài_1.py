while True:
    n = int(input("Nhập n nguyên dương: "))
    if n > 0: break
    print("Nhập lại n!")

s4 = s5 = s6 = 0
i = 1
while i <= n:
    s4 += i**2
    s5 += (2*i - 1)**3  
    s6 += (2*i)**4      
    i += 1
s5 += (2*n + 1)**3 

print(f"S4={s4}, S5={s5}, S6={s6}")