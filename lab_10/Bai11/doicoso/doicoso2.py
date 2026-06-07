def loc_chuoikytu(chuoikytu):
    chars = {"0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"}
    result = ""
    for c in chuoikytu:
        if c in chars:
            result += c
    return result

def detect_hecoso(chuoikytu):
    if all(c in "01" for c in loc_chuoikytu(chuoikytu)):
        return "Hệ nhị phân"
    elif all(c in "01234567" for c in loc_chuoikytu(chuoikytu)):
        return "Hệ bát phân"
    elif all(c in "0123456789ABCDEF" for c in loc_chuoikytu(chuoikytu)):
        return "Hệ thập lục phân"
    else:
        return "Không xác định được hệ cơ số"
    
def convert_binary_to_decimal(chuoikytu):
    if detect_hecoso(chuoikytu) != "Hệ nhị phân":
        return "Chuỗi không phải là hệ nhị phân"
    decimal_value = 0
    for i, c in enumerate(reversed(loc_chuoikytu(chuoikytu))):
        decimal_value += int(c) * (2 ** i)
    return f"Giá trị thập phân: {decimal_value}"
    
def convert_octal_to_decimal(chuoikytu):
    if detect_hecoso(chuoikytu) != "Hệ bát phân":
        return "Chuỗi không phải là hệ bát phân"
    decimal_value = 0
    for i, c in enumerate(reversed(loc_chuoikytu(chuoikytu))):
        decimal_value += int(c) * (8 ** i)
    return f"Giá trị thập phân: {decimal_value}"

def convert_hexadecimal_to_decimal(chuoikytu):
    if detect_hecoso(chuoikytu) != "Hệ thập lục phân":
        return "Chuỗi không phải là hệ thập lục phân"
    decimal_value = 0
    hex_digits = "0123456789ABCDEF"
    for i, c in enumerate(reversed(loc_chuoikytu(chuoikytu))):
        decimal_value += hex_digits.index(c) * (16 ** i)
    return f"Giá trị thập phân: {decimal_value}"
