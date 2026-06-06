# Bài tập tuần 9:
# Bài 1:Tìm số lớn nhất trong 3 số
def max_of_three(a, b, c):
    if a >= b and a >= c: return a
    if b >= a and b >= c: return b
    return c

#==============================================
# Bài 2: Tìm ước chung lớn nhất của n số:
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def gcd_of_list(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result

#==============================================
# Bài 3: Lũy thừa:
def power(a, n):
    if n == 0: return 1
    return a * power(a, n - 1)

#==============================================
# Bài 4: Nhập từ bàn phím và in ra hoán vị của [1,2,...,n]
def permute(nums):
    if len(nums) == 1: return [nums]
    perms = []
    for i in range(len(nums)):
        for p in permute(nums[:i] + nums[i+1:]):
            perms.append([nums[i]] + p)
    return perms
def print_permutations(n):
    nums = list(range(1, n + 1))
    for p in permute(nums):
        print(p)

#==============================================
# Bài 5: Tính đệ qui:
def permutation(arr):
    if len(arr) == 1: return [arr]
    result = []
    for i in range(len(arr)):
        m = arr[i]
        rem_list = arr[:i] + arr[i+1:]
        for p in permutation(rem_list):
            result.append([m] + p)
    return result

#==============================================
# Bài 6: Hoán vị ngẫu nhiên:
import random
def hoan_vi(arr):
    for i in range(len(arr)-1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

#==============================================
# Bài 7: Nghiệm phương trình N = x_1 + x_2 + ... + xn:
def nghiem(N, n):
    if n == 1: return [[N]]
    result = []
    for i in range(N + 1):
        for p in nghiem(N - i, n - 1):
            result.append([i] + p)
    return result

#==============================================
# Bài 8:
# a. S = 1/(1*2) + ... + 1/(n*(n+1))
def sum_a(n):
    if n == 1: return 1/2
    return sum_a(n-1) + 1/(n*(n+1))

# b. S = 1/1! + ... + 1/n!
import math
def sum_b(n):
    if n == 1: return 1
    return sum_b(n-1) + 1/math.factorial(n)

# c. S = sqrt(3n + sqrt(3(n-1) + ... + sqrt(3+sqrt(6+sqrt(3)))))
def sum_c(n, current=1):
    if current == n: return (3*current)**0.5
    return (3*n + sum_c(n-1, current))**0.5 # Logic đệ quy cần căn chỉnh theo cấu trúc lồng

# d. S = sqrt(n + sqrt(n-1 + ... + sqrt(2 + sqrt(1))))
def sum_d(n):
    if n == 1: return 1
    return (n + sum_d(n-1))**0.5

#==============================================
# Bài 9: Đảo ngược số:
def reverse_num(n, rev=0):
    if n == 0: return rev
    return reverse_num(n // 10, rev * 10 + n % 10)

#==============================================
# Bài 10: Tính dãy X:
def x_n(n):
    if n == 0: return 1
    return sum(((n - k)**2 * x_n(k) for k in range(n)))

#==============================================
# Bài 11: Giai thừa kép:
def kep(n):
    if n == 0 or n == 1: return 1
    return kep(n - 2) * n

#==============================================
# Bài 12: 
def giai(ga, cho):
    if ga + cho == 36 and 2 * ga + 4 * cho == 100:
        return ga, cho
    if ga + cho > 36: return None
    # Thử đệ quy tăng số lượng
    res = giai(ga + 1, cho)
    if res: return res
    return giai(ga, cho + 1)

