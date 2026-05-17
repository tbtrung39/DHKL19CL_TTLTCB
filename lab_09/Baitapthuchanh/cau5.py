def hoan_vi(ds):
    if len(ds) == 1:
        return [ds]
    kq = []
    for i in range(len(ds)):
        for p in hoan_vi(ds[:i] + ds[i+1:]):
            kq.append([ds[i]] + p)
    return kq
n = input("Nhap n: ")
n = int(n)
ds = list(range(1, n + 1))
result = hoan_vi(ds)
for item in result:
    print(item)
    # Giai thich:
# vd nhap n = 3 -> ds = [1, 2, 3] -> hoan_vi([1, 2, 3]) -> i = 0, vtri = 1 -> ds_con = [2, 3] -> kq_con = hoan_vi([2, 3]) -> i = 0, vtri = 2 -> ds_con = [3] -> kq_con = hoan_vi([3]) -> return [[3]] -> kq.append([2] + [3]) -> kq.append([2, 3])
#                                                                                                                         -> i = 1, vtri = 3 -> ds_con = [2] -> kq_con = hoan_vi([2]) -> return [[2]] -> kq.append([3] + [2]) -> kq.append([3, 2])
#                                                                                                                         -> return [[2, 3], [3, 2]] 
#                                                                                                                         -> kq.append([1] + [2, 3]) -> kq.append([1, 2, 3]) 
#                                                                                                                         -> kq.append([1] + [3, 2]) -> kq.append([1, 3, 2])
#                                                       -> i = 1, vtri = 2 -> ds_con = [1, 3] -> kq_con = hoan_vi([1, 3]) -> i = 0, vtri = 1 -> ds_con = [3] -> kq_con = hoan_vi([3]) -> return [[3]] -> kq.append([1] + [3]) -> kq.append([1, 3])
#                                                                                                                         -> i = 1, vtri = 3 -> ds_con = [1] -> kq_con = hoan_vi([1]) -> return [[1]] -> kq.append([3] + [1]) -> kq.append([3, 1])
#                                                                                                                         -> return [[1, 3], [3, 1]]
#                                                                                                                         -> kq.append([2] + [1, 3]) -> kq.append([2, 1, 3])
#                                                                                                                         -> kq.append([2] + [3, 1]) -> kq.append([2, 3, 1])
#                                                      -> i = 2, vtri = 3 -> ds_con = [1, 2] -> kq_con = hoan_vi([1, 2]) -> i = 0, vtri = 1 -> ds_con = [2] -> kq_con = hoan_vi([2]) -> return [[2]] -> kq.append([1] + [2]) -> kq.append([1, 2])
#                                                                                                                         -> i = 1, vtri = 2 -> ds_con = [1] -> kq_con = hoan_vi([1]) -> return [[1]] -> kq.append([2] + [1]) -> kq.append([2, 1])
#                                                                                                                         -> return [[1, 2], [2, 1]]
#                                                                                                                         -> kq.append([3] + [1, 2]) -> kq.append([3, 1, 2])
#                                                                                                                         -> kq.append([3] + [2, 1]) -> kq.append([3, 2, 1])  
# chay vong for item trong result -> print ket qua                     