cpp = set()
java = set()
python = set()
a = int(input("Nhập số SV thi C++: "))
for i in range(a):
    x = int(input("Nhập mã SV: "))
    cpp.add(x)
b = int(input("Nhập số SV thi Java: "))
for i in range(b):
    x = int(input("Nhập mã SV: "))
    java.add(x)
c = int(input("Nhập số SV thi Python: "))
for i in range(c):
    x = int(input("Nhập mã SV: "))
    python.add(x)
# Thi đúng 1 ngôn ngữ
mot = (cpp - java - python) | (java - cpp - python) | (python - cpp - java)
# Thi đúng 2 ngôn ngữ
hai = ((cpp & java) | (cpp & python) | (java & python)) - (cpp & java & python)
# Thi cả 3 ngôn ngữ
ba = cpp & java & python
print("Sinh viên thi 1 ngôn ngữ: ", mot)
print("Sinh viên thi 2 ngôn ngữ: ", hai)
print("Sinh viên thi 3 ngôn ngữ: ", ba)