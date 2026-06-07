# bài 6:
def xu_ly_bang_so():
    noi_dung = """4
                211 133 180 5
                192 168 1 254
                11 1 11 233
                10 20 30 40""" 
    
    file_name = "bang_so.txt"
    with open(file_name, "w") as f:
        f.write(noi_dung)

    
    with open(file_name, "r") as f:
        lines = f.readlines()
        matrix = [list(map(int, line.split())) for line in lines[1:]]

    
    print("Dòng 1:", matrix[0])
    print("Dòng 3:", matrix[2])

    
    print("\nNội dung toàn bộ file:")
    for row in matrix:
        print(row)

    
    with open("ODD.txt", "w") as f:
        for row in matrix:
            # Nếu là số lẻ giữ nguyên, nếu chẵn thay bằng 0
            new_row = [str(x) if x % 2 != 0 else '0' for x in row]
            f.write(" ".join(new_row) + "\n")
    print("\nĐã ghi ma trận số lẻ vào ODD.txt")

    print("\nDòng cuối cùng của file:", lines[-1].strip())

xu_ly_bang_so()