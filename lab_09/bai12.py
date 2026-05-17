def giai_ga_cho(so_ga):
    if so_ga > 36:
        return None
    
    so_cho = 36 - so_ga
    if (so_ga * 2 + so_cho * 4) == 100:
        return so_ga, so_cho
        
    return giai_ga_cho(so_ga + 1)

ket_qua = giai_ga_cho(0)
print(f"Gà: {ket_qua[0]}, Chó: {ket_qua[1]}")