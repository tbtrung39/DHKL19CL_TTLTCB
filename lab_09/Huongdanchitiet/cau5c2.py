def sum_recursive(n,result):
    current_sum = 0
    current_list = []
    def helper(n, current_sum, current_list):
        if current_sum == n :
            result.append(current_list)
            return
        for i in range(1, n + 1):
            if current_sum + i <= n:
                helper(n, current_sum + i, current_list + [i])
    helper(n, current_sum, current_list)
    return result
n = int(input("Nhap so tu nhien N: "))
result = sum_recursive(n, [])
for item in result:
    print("%d = %s" % (n, " + ".join(map(str, item))))
# Giai thich:
# vd nhap n = 3 -> result = sum_recursive(3, []) -> helper(3, 0, []) 
# Nhanh 1: 0 != 3-> chay for lan 1: i = 1 -> helper(3, 1, [1]) -> 1!= 3 -> chay for lan 2: i = 1 -> helper(3, 2, [1,1]) -> 2 != 3-> chay for lan 3:i = 1 -> helper(3, 3, [1, 1, 1]) -> 3 == 3 -> result.append([1, 1, 1])
#                                                                                          i = 2 -> helper(3, 3, [1,2]) -> helper(3, 3, [1,2])-> result.append([1,2]) 
# Nhanh 2: 0 != 3 -> chay for lan 1: i = 2 -> helper(3, 2, [2]) -> 2 != 3 -> chay for lan 2: i = 1 -> helper(3, 3, [2,1]) -> 3 == 3 -> result.append([2,1])
# Nhanh 3: 0 != 3 -> chay for lan 1: i = 3 -> helper(3, 3, [3]) -> 3 == 3 -> result.append([3])
# chay vong for item trong result -> print ket qua