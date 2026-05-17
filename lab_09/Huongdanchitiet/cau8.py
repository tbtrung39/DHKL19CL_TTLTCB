def find_solution(n, x1, x2, x3):
    if x1 + x2 + x3 == n:
        print(x1, x2, x3)
        return
    if x1 + x2 + x3 < n:
        find_solution(n, x1 + 1, x2, x3)
        find_solution(n, x1, x2 + 1, x3)
        find_solution(n, x1, x2, x3 + 1)
N = int(input("Nhap so tu nhien N: "))
print("Cac nghiem cua phuong trinh N = x1 + x2 + x3 la: ")
find_solution(N, 0, 0, 0)
# Giai thich:
# vd nhap n = 2 
# -> find_solution(2, 0, 0, 0) 
# -> x1 + x2 + x3 = 0 
# -> chay 3 lan de tang x1, x2, x3 len 1 -> find_solution(2, 1, 0, 0) -> x1 + x2 + x3 = 1 -> chay 3 lan de tang x1, x2, x3 len 2 -> find_solution(2, 2, 0, 0) -> x1 + x2 + x3 = 2 -> print(2, 0, 0)
#                                                                                         -> find_solution(2, 1, 1, 0) -> x1 + x2 + x3 = 2 -> print(1, 1, 0)
#                                                                                         -> find_solution(2, 1, 0, 1) -> x1 + x2 + x3 = 2 -> print(1, 0, 1)
#                                                                                         -> find_solution(2, 0, 2, 0) -> x1 + x2 + x3 = 2 -> print(0, 2, 0)
#                                                                                         -> find_solution(2, 0, 1, 1) -> x1 + x2 + x3 = 2 -> print(0, 1, 1)
#                                                                                         -> find_solution(2, 0, 0, 2) ->   x1 + x2 + x3 = 2 -> print(0, 0, 2)