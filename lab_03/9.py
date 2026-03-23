n = int(input("nhập số:"))
if n <= 0 :
    print("số nhập vào phải lớn hơn 0")

tonga=0
for i in range(1,n+1):
    tonga = i**2 + tonga
print("tổng a là: ",tonga)

tongb=0
for k in range(1 ,n+1):
    tongb = (2*k+1)**3 + tongb
print("tổng b là: ",tongb)

tongc=0
for j in range(1,n+1):
    tongc = (2*j)**4 + tongc
print("tổng c là: ",tongc)