def print_int(n):
    print(f"Kết quả: {n}")

def convert_to_binary(n):
    if n < 0:
        return "Không thể chuyển đổi số âm sang nhị phân"
    elif n == 0:
        return print_int(0)
    else:
        binary = ""
        while n > 0:
            binary = str(n % 2) + binary
            n //= 2
        return print_int(int(binary))
    
def convert_to_octal(n):
    if n < 0:
        return "Không thể chuyển đổi số âm sang bát phân"
    elif n == 0:
        return print_int(0)
    else:
        octal = ""
        while n > 0:
            octal = str(n % 8) + octal
            n //= 8
        return print_int(int(octal))

def convert_to_hexadecimal(n):
    if n < 0:
        return "Không thể chuyển đổi số âm sang thập lục phân"
    elif n == 0:
        return print_int(0)
    else:
        hexadecimal = ""
        hex_digits = "0123456789ABCDEF"
        while n > 0:
            hexadecimal = hex_digits[n % 16] + hexadecimal
            n //= 16
        return print_int(int(hexadecimal, 16))