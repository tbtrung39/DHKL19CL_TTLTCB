import random

List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]

#1
for x in List_:
    print(x)

#2
print(List_[1])
print(List_[1][1])

#3
print(len(List_))
new = [random.randint(1,200)]
List_.append(new)
print(List_)

#4
sum = List_[1][1] + List_[2][1] + List_[5][1] + List_[6][1]