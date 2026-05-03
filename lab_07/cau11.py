n = input("Nhập số sinh viên của trường: ")
n = int(n)
a = input("Số sinh viên thi C++: ")
a = int(a)
CPP = set()
i = 0
while i < a:
    x = input("Nhập số thứ tự sinh viên thi C++: ")
    CPP.add(x)
    i = i + 1
b = input("Số sinh viên thi Java: ")
b = int(b)
JAVA = set()
i = 0
while i < b:
    x = input("Nhập số thứ tự sinh viên thi Java: ")
    JAVA.add(x)
    i = i + 1
c = input("Số sinh viên thi Python: ")
c = int(c)
PYTHON = set()
i = 0
while i < c:
    x = input("Nhập số thứ tự sinh viên thi Python: ")
    PYTHON.add(x)
    i = i + 1
thi_ca_3 = CPP & JAVA & PYTHON
hai_nn = (CPP & JAVA) | (CPP & PYTHON) | (JAVA & PYTHON)
hai_nn = hai_nn - thi_ca_3
mot_nn = (CPP | JAVA | PYTHON) - hai_nn - thi_ca_3
print("Sinh viên thi cả 3 môn:", thi_ca_3)
print("Sinh viên thi 2 môn:", hai_nn)
print("Sinh viên chỉ thi 1 môn:", mot_nn)