Str = """Python là một ngôn ngữ lập trình mạnh mẽ. 
Lập trình Python rất thú vị và Python cũng rất dễ học.
Học lập trình không khó, chỉ cần chăm chỉ."""

find_word = input('Nhập từ cần tìm: ').strip()
split_words = Str.split()

total_count = 0
for word in split_words:
    if find_word in word:
        total_count += 1

print(f'Từ "{find_word}" xuất hiện {total_count} lần trong chuỗi.')