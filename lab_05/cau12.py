str = input('nhap chuoi: ')
chu = ""
for i in str:
    if i == " " or i == ",":
        if chu != "":
            print(chu)
            chu = ""
    else:
        chu = chu +chu

if chu != "":
    print(chu)