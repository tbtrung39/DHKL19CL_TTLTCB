#su dung module random va list comprehension de xuat mot so ngau nhien ,chia het cho 5 va 7, tu 0 den 200(gom ca 0 va 200)
import random
n = [x for x in range(201) if x % 5 == 0 and x % 7 == 0]
random_number = random.choice(n)
print("So ngau nhien chia het cho 5 va 7 tu 0 den 200: ", random_number)