list1 = [101, 102, 103]
list2 = ["An", "Bình", "Chi"]
res_dict = {}

n = len(list1) if len(list1) < len(list2) else len(list2)
for i in range(n):
    res_dict[list1[i]] = list2[i]

print("\nBài 15:")
for k in res_dict:
    print(f"<{k}>: <{res_dict[k]}>")