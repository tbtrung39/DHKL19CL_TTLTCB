List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]

#in cac phan tu trong List_ 
for i in List_:
    print(i)
#chon ra phan tu thu 2, thuoc vi tri thu 3 cua sublist
print("Phan tu thu 2 cua sublist thu 3 la: ", List_[2][1])
#kiem tra do dai cua List_
print("Do dai cua List_ la: ", len(List_))
#them mot sublist ngau nhien vao list
import random
new_sublist = ["new_day", random.randint(1, 150)]
List_.append(new_sublist)
print("List_ sau khi them sublist moi la: ", List_)
#tinh tong sale value cua List_ trong thu 2,3,7 ,cn
total_sale = List_[1][1] + List_[2][1] + List_[6][1] + List_[7][1]
print("Tong sale value cua List_ trong thu 2,3,7 ,cn la: ", total_sale)
