def hanoi_tower(n,from_column, to_column, using_column):
    if n == 1:
        print("Dich chuyen dia 1 tu cot",from_column,"den cot", to_column)
        return
    hanoi_tower(n-1, from_column, using_column, to_column)
    print("Dich chuuyen dia", n, "tu cot", from_column, "den cot", to_column)
    hanoi_tower(n-1, using_column, to_column, from_column)
n = int(input("Nhap vao so dia can dich chuyen: "))
hanoi_tower(n, 'A', 'B', 'C')
# Giai thich:   
# vd nhap n = 2 
# -> hanoi_tower(2, 'A', 'B', 'C') 
# -> hanoi_tower(1, 'A', 'C', 'B') 
# -> print("Dich chuyen dia 1 tu cot A den cot B") 
# -> hanoi_tower(1, 'B', 'C', 'A') 
# -> print("Dich chuyen dia 1 tu cot B den cot C") 
# -> print("Dich chuuyen dia 2 tu cot A den cot C") 
# -> hanoi_tower(1, 'A', 'C', 'B') 
# -> print("Dich chuyen dia 1 tu cot A den cot C")    
