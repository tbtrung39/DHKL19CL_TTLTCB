def input_items():
    items = []
    while True:
        try:
            n = int(input('Nhập số mặt hàng: '))
            if n <= 0:
                print('Phải nhập số nguyên dương. Thử lại.')
                continue
            break
        except ValueError:
            print('Vui lòng nhập số nguyên. Thử lại.')
    for i in range(n):
        print(f'-- Mặt hàng {i+1} --')
        while True:
            code = input('Mã hàng (4 ký tự): ').strip()
            if len(code) != 4:
                print('Mã hàng phải có đúng 4 ký tự. Thử lại.')
                continue
            break
        name = input('Tên hàng: ').strip()
        unit = input('Đơn vị tính: ').strip()
        while True:
            try:
                price = float(input('Đơn giá: '))
                break
            except ValueError:
                print('Đơn giá là số. Thử lại.')
        while True:
            try:
                qty = int(input('Số lượng: '))
                break
            except ValueError:
                print('Số lượng là số nguyên. Thử lại.')
        amount = price * qty
        vat = amount * 0.10
        items.append({'code': code, 'name': name, 'unit': unit, 'price': price, 'qty': qty, 'amount': amount, 'vat': vat})
    return items


def compute_amounts(items):
    for it in items:
        it['amount'] = it['price'] * it['qty']
        it['vat'] = it['amount'] * 0.10
    return items


def sort_by_vat_desc(items):
    return sorted(items, key=lambda x: x['vat'], reverse=True)


def print_items(items):
    header = f"{'Mã':4} {'Tên':20} {'Đv':6} {'Đơn giá':10} {'Số lượng':8} {'Thành tiền':12} {'Thuế':10}"
    print(header)
    for it in items:
        print(f"{it['code']:4} {it['name'][:20]:20} {it['unit'][:6]:6} {it['price']:10.2f} {it['qty']:8d} {it['amount']:12.2f} {it['vat']:10.2f}")
