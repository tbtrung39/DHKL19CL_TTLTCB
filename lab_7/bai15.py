list1 = [101, 102, 103, 104]
list2 = ["An", "Bình", "Cường", "Dương"]
dictionary_zip = dict(zip(list1, list2))
print("Cách 1 (Dùng zip):", dictionary_zip)
dictionary_loop = {}
for i in range(len(list1)):
    dictionary_loop[list1[i]] = list2[i]
    
print("Cách 2 (Dùng vòng lặp):", dictionary_loop)