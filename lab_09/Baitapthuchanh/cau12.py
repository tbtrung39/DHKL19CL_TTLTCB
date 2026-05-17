def tim(x, y):
    if x + y == 36 and 2 * x + 4 * y == 100:
        print("So ga =", x)
        print("So cho =", y)
        return
    tim(x + 1, y - 1)
tim(0, 36)
# Giải thích:
# Ban dau x = 0, y = 36 
# -> moi lan xoay vong x tang 1, y giam 1
# -> cho den khi x + y = 36 va 2 * x + 4 * y = 100 thi dung lai 
# -> in ra ket qua x = 22 va y = 14 