def count_characters_recursive(string ,count):
    if not string:
        return count
    if string[0].isalpha():
        count['alphabet'] = count['alphabet'] + 1
    elif string[0].isdigit():
        count['digit'] = count['digit'] + 1
    else:
        count['special'] = count['special'] + 1
    return count_characters_recursive(string[1:], count)
string = input("Nhap chuoi ky tu: ")
count = {'alphabet': 0, 'digit': 0, 'special': 0}
count = count_characters_recursive(string, count)
print("So luong ky tu chu cai: ", count['alphabet'])
print("So luong ky tu so: ", count['digit'])
print("So luong ky tu dac biet: ", count['special'])
# Giai thich:
# vd nhap string = "abc123!@#" -> count_characters_recursive("abc123!@#", {'alphabet': 0, 'digit': 0, 'special': 0}) 
# -> count_characters_recursive("bc123!@#", {'alphabet': 1, 'digit': 0, 'special': 0}) 
# -> count_characters_recursive("c123!@#", {'alphabet': 2, 'digit': 0, 'special': 0}) 
# -> count_characters_recursive("123!@#", {'alphabet': 3, 'digit': 0, 'special': 0}) 
# -> count_characters_recursive("23!@#", {'alphabet': 3, 'digit': 1, 'special': 0}) 
# -> count_characters_recursive("3!@#", {'alphabet': 3, 'digit': 2, 'special': 0}) 
# -> count_characters_recursive("!@#", {'alphabet': 3, 'digit': 3, 'special': 0}) 
# -> count_characters_recursive("@#", {'alphabet': 3, 'digit': 3, 'special': 1}) 
# -> count_characters_recursive("#", {'alphabet': 3, 'digit': 3, 'special': 2}) 
# -> count_characters_recursive("", {'alphabet': 3, 'digit': 3, 'special': 3}) 
# -> return {'alphabet': 3, 'digit': 3, 'special': 3}
# chay print ket qua