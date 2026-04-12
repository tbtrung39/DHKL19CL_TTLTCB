A, B, C = ["Anh", "Em"], ["Chơi", "Yêu"], ["Bóng đá", "Bóng rổ"]
print(*(f"{a} {b} {c}." for a in A for b in B for c in C), sep="\n")